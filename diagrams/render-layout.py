"""Apply layout-only corrections to locally rendered PlantUML SVG and PNG files.

Run after PlantUML export. The .puml files stay unchanged. Requires lxml,
Pillow, and Node.js with Sharp (provide --sharp-module if it is not on NODE_PATH).
PNG PlantUML source metadata is preserved.
"""
from pathlib import Path
from lxml import etree as E
from PIL import Image
import argparse, hashlib, json, re, struct, subprocess

NS = {"s": "http://www.w3.org/2000/svg"}
PAD = 20.0
SHARP_JS = """const sharp = require(process.argv[3] || 'sharp');
sharp(process.argv[1]).flatten({background: "#ffffff"}).png().toFile(process.argv[2])
.then(() => {}).catch(e => { console.error(e.message); process.exit(1); });"""

def f(value):
    return float(value.removesuffix("px"))

def fmt(value):
    return ("%.3f" % value).rstrip("0").rstrip(".")

def all_text(tree):
    return ["".join(t.itertext()) for t in tree.xpath("//s:text", namespaces=NS)]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def png_chunks(raw):
    assert raw[:8] == b"\x89PNG\r\n\x1a\n"
    pos = 8
    while pos < len(raw):
        length = struct.unpack(">I", raw[pos:pos+4])[0]
        chunk = raw[pos:pos+length+12]
        yield raw[pos+4:pos+8], raw[pos+8:pos+8+length], chunk
        pos += length+12

def fix_sequence(tree, source):
    entities = dict((alias, label) for label, alias in
                    re.findall(r'^entity\s+"([^"]+)"\s+as\s+(\w+)', source, re.M))
    created = set(re.findall(r'(?:->|-->>)\s+(\w+)\s+\*\*\s*:', source))
    labels = set(part for alias in created if alias in entities
                 for part in entities[alias].split(r"\n"))
    texts = [t for t in tree.xpath("//s:text", namespaces=NS)
             if "".join(t.itertext()) in labels]
    frames = {}
    for rect in tree.xpath('//s:rect[@fill="none"]', namespaces=NS):
        if rect.get("rx") or "stroke-width:2.344" not in rect.get("style", ""):
            continue
        key = tuple(f(rect.get(a)) for a in ("x", "y", "width", "height"))
        frames.setdefault(key, []).append(rect)
    rights = {k: k[0]+k[2] for k in frames}
    reasons = {k: [] for k in frames}
    for key in frames:
        x, y, width, height = key
        old_right = x+width
        for t in texts:
            tx, ty = f(t.get("x")), f(t.get("y"))
            length = f(t.get("textLength", "0"))
            if x <= tx < old_right and y < ty < y+height:
                desired = tx+length+PAD
                if desired > old_right:
                    rights[key] = max(rights[key], desired)
                    reasons[key].append("Clear object label: "+"".join(t.itertext()))
    # Preserve containment for nested fragments after an inner frame expands.
    for child in sorted(frames, key=lambda k:k[3]):
        cx, cy, cw, ch = child
        for parent in frames:
            px, py, pw, ph = parent
            if parent == child:
                continue
            if (px <= cx and py <= cy and cy+ch <= py+ph
                    and cx+cw <= px+pw and ph > ch):
                desired = rights[child]+16
                if rights[child] > cx+cw and desired > rights[parent]:
                    rights[parent] = desired
                    reasons[parent].append("Keep expanded child fragment inside")
    changes = []
    for key, rects in frames.items():
        x, y, width, height = key
        old_right, new_right = x+width, rights[key]
        if new_right <= old_right+0.001:
            continue
        for rect in rects:
            rect.set("width", fmt(new_right-x))
        for line in tree.xpath("//s:line", namespaces=NS):
            if (abs(f(line.get("x1", "-1"))-x) < .01
                    and abs(f(line.get("x2", "-1"))-old_right) < .01
                    and y <= f(line.get("y1", "-1")) <= y+height
                    and abs(f(line.get("y1", "-1"))-f(line.get("y2", "-2"))) < .01):
                line.set("x2", fmt(new_right))
        changes.append({"kind":"fragment_width", "x":x, "y":y,
                        "old_right":old_right, "new_right":new_right,
                        "reason":reasons[key]})
    if changes:
        root = tree.getroot()
        width = f(root.get("width"))
        needed = max(c["new_right"] for c in changes)+20
        if needed > width:
            root.set("width", fmt(needed)+"px")
            viewbox = root.get("viewBox").split()
            viewbox[2] = fmt(needed)
            root.set("viewBox", " ".join(viewbox))
            root.set("style", re.sub(r"width:[\d.]+px", "width:"+fmt(needed)+"px", root.get("style","")))
    return changes

def fix_class(tree):
    entities = {g.get("data-qualified-name"):g for g in
                tree.xpath('//s:g[@class="entity"]', namespaces=NS)}
    staff = entities["Staff"]
    staff_id = staff.get("id")
    box = staff.find("s:rect", NS)
    staff_y = f(box.get("y"))
    labels = []
    for g in tree.xpath('//s:g[@class="link"]', namespaces=NS):
        if g.get("data-entity-1") != staff_id:
            continue
        target = g.get("data-entity-2")
        if target not in [entities[n].get("id") for n in ("Standby","JobPreference","LeaveRequest")]:
            continue
        for t in g.findall("s:text", NS):
            if "".join(t.itertext()) == "1" and staff_y-100 < f(t.get("y")) < staff_y:
                labels.append(t)
    if len(labels) != 3 or max(f(t.get("y")) for t in labels)-min(f(t.get("y")) for t in labels) > 4:
        return []
    changes = []
    for t, offset in zip(sorted(labels,key=lambda t:f(t.get("x"))), (-66,-33,0)):
        if offset:
            old_y=f(t.get("y"))
            t.set("y",fmt(old_y+offset))
            changes.append({"kind":"multiplicity_label_position","text":"1",
                            "x":f(t.get("x")),"old_y":old_y,"new_y":old_y+offset})
    return changes

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--puml-dir",type=Path,default=Path(__file__).parent)
    ap.add_argument("--render-dir",type=Path)
    ap.add_argument("--report",type=Path,required=True)
    ap.add_argument("--node",default="node")
    ap.add_argument("--sharp-module",default="")
    args=ap.parse_args()
    sources=args.puml_dir.resolve()
    renders=(args.render_dir or sources/"out").resolve()
    results=[]
    for puml in sorted(sources.glob("SD-*.puml"))+[sources/"CD-domain.puml"]:
        svg=renders/(puml.stem+".svg"); png=renders/(puml.stem+".png")
        source_before=puml.read_bytes()
        svg_before=svg.read_bytes()
        tree=E.fromstring(svg_before).getroottree()
        text_before=all_text(tree)
        changes=(fix_sequence(tree,source_before.decode("utf-8")) if puml.name.startswith("SD-")
                 else fix_class(tree))
        if changes:
            assert all_text(tree)==text_before, "SVG text changed"
            svg.write_bytes(E.tostring(tree,encoding="utf-8"))
            png_before=png.read_bytes()
            metadata=[chunk for typ,data,chunk in png_chunks(png_before)
                      if typ in (b"iTXt", b"tEXt", b"zTXt") and data.startswith(b"plantuml\0")]
            temp=renders/(puml.stem+".layout-temp.png")
            assert temp.parent==renders
            subprocess.run([args.node,"-e",SHARP_JS,str(svg),str(temp),args.sharp_module],
                           check=True)
            rendered=temp.read_bytes()
            if metadata:
                chunks=list(png_chunks(rendered))
                png.write_bytes(rendered[:8]+b"".join(c for typ,d,c in chunks
                    if not (typ in (b"iTXt", b"tEXt", b"zTXt") and d.startswith(b"plantuml\0")) and typ!=b"IEND")
                    +b"".join(metadata)+next(c for typ,d,c in chunks if typ==b"IEND"))
            else:
                png.write_bytes(rendered)
            temp.unlink()
            with Image.open(png) as im:
                im.verify()
            assert puml.read_bytes()==source_before, "PlantUML source changed"
            assert all_text(E.parse(svg))==text_before, "Serialized SVG text changed"
            assert all(c in png.read_bytes() for c in metadata)
        results.append({"diagram":puml.stem,"changes":changes,
                        "source_sha256":sha(source_before),
                        "svg_text_preserved":True,
                        "png_plantuml_metadata_preserved":True,
                        "svg_before_sha256":sha(svg_before),
                        "svg_after_sha256":sha(svg.read_bytes())})
    args.report.write_text(json.dumps({"method":"Local SVG layout correction; no source or text edits",
                                      "diagrams":results},indent=2),encoding="utf-8")
    print("Layout corrected for:",", ".join(r["diagram"] for r in results if r["changes"]))
    print("All PlantUML sources, SVG text, and PNG source metadata preserved.")

if __name__=="__main__":
    main()
