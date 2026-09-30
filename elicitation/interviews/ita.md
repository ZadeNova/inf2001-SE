# IT Administrator

## Accounts and permissions

Interviewer: Can you walk me through how a new employee should receive an account and the appropriate access?

IT admin: When employees are being created in our current employee management system, we will also add them to the scheduling system. Ideally, we manually create the user so as to ensure correctness in our procedures and details. Normal employees such as drivers or technicians will have access to adding and editing of their own schedules. Managers will have access to other peoples schedules.

IT admin: IT admins need to be able to edit the permissions of other accounts.

Interviewer: Good, what information is required to create a staff or manager account?

IT admin: All accounts will be need name, email, default password that user can change later. For managers specifically, they need to have special permissions as said before but other than that, I don’t think any special information is needed for account creation.

Interviewer: I see, so all accounts are made the same and then permissions are added after. How should access permissions be assigned and changed?

IT admin: Only the IT admins should have any permissions to grant or edit access permissions. Managers will not be able to grant any permissions, but they will have special permissions to be able to edit and look through all employee schedules. Normal employees will can only manage their own.

Interviewer: What should happen to an account when someone changes role or leaves the company?

IT admin: Oh, this is simple, for changing of roles the IT admin will change the permissions according to what they should have. If they leave then, IT admin will delete their account. If they had any outstanding schedules, those should be removed when the account is deleted.

Interviewer: How should forgotten passwords or access problems be handled?

IT admin: This one is like other websites or apps, they click “forget password” which will send a confirmation to their company email the request for changing password. From there they will edit the password on the platform. For access problems that one is a bit vague, but for scenarios like forgot username or account locked due to too many tries, they must email or directly talk to the IT admin in person to help them. Only IT admins should fix this.

Interviewer: What user actions or record changes need an audit history?

IT admin: Audit history? Oh that, for that we should see all account detail changes, password change requests. Full logs of the schedule changes should be recorded as well. This is important to check for any bad actors, if they lie and they didn’t edit the schedule, we can pull out the records in the event of it being needed. Both staff and managers can lie so we need to be impartial.

Interviewer: What safeguards are needed to prevent unauthorised access to staff information?

IT admin: 2FA when logging in would be good, send confirmation to user email before they can login. On the scheduler the only things that should be displayed are the names and emails of who put their schedule in that timeslot. All data related to staff information and timing should be encrypted properly in the backend.

Interviewer: Ok, and how many users should the system support at the same time during busy periods?

IT admin: Since the company is not very big, about less than 50 people, we should try to support 50 or so. I believe it is important to have a bit more in case the same person login from multiple devices or try to keep refreshing which can send multiple batches of data. We need to also have rate limits to prevent things like high volumes of requests.

Interviewer: What response-time targets are practical for the main user actions?

IT admin: Give me some time to think about this.

IT admin: Ok, it should be a fast but doesn’t need to be very fast. The user just needs to be aware that the site is responsive. Since it’s scheduling exact seconds aren’t important so something like maybe 3 or 5 seconds will be enough per schedule request. Then it should be reflected in the scheduler in less than a minute or so.

Interviewer: During which hours must the system be available?

IT admin: 24/7. Peak periods would be Monday since the employees will want to see their allocations, and they will all login during that time. Usually, timing would be about early morning before work starts. Another peak period would be Thursday since they can start scheduling their slots then.

Interviewer: How long could an outage last before it seriously disrupts operations?

IT admin: Not more than one day. The schedule is very important to our staff. Not all of them will take a screenshot of the schedule, so if they will need to login to the system to find out their daily assignments. Without it we may miss crucial dates or times with our clients. In this kind of case, an offline backup that is updated every hour or so will be helpful to prevent all of them from not knowing their next client and timings. There will be scheduled downtime like maintenance but this one which usually happens early morning or late night, it will usually not affect users.

Interviewer: Alright, what should happen to information being entered if the connection or system fails?

IT admin: In this kind of scenario, if possible, it should try to hold it until it can submit it but otherwise if data is lost, it needs to inform the user that the request failed and that they should contact IT admin or try again later.

Interviewer: Right, so now we have some recovery questions.

Interviewer: How quickly should the system and its data be restored after a failure?

IT admin: Well, this one normally depends on severity of data loss, but generally same as outage, not one whole day of downtime. If we have the backups then it should not be that big of an issue, maybe losing an hour of schedule updates is not very impactful. So, we can just tell them to update it again.

Interviewer: What rules should govern the retention and deletion of records?

IT admin: All schedules should exist up to one year in our system, we need to be able to track our staff and their movements for each yearly review. Deletion of past or currently happening schedules should not be possible, but if they have yet to pass then deletion should be ok.

IT admin: For employee details, only IT admin can delete their records with the same rules as stated before.

Interviewer: What devices and browsers must the application support?

IT admin: All the classic ones that people use nowadays, chrome is most important since all our staff use it. Edge, Firefox, DuckDuckGo, etc. Devices should be our company laptops and tablets, as well as all modern phones.

Interviewer: What existing systems, if any, must exchange information with this application?

IT admin: We have our current employee portal that should have existing employees inside, so we need to have all employees from that ported over. We have our employees and current schedules be able to be exported in CSV format so that can help with transferring data.

Interviewer: Ok, with that just a few closing questions.

Interviewer: Are there important issues have we not covered?

IT admin: Not that I’m aware of.

Interviewer: Which of the needs discussed matters most to you, and why?

IT admin: The access permission allocation, backups, and transferring of old data into the new system. The first 2 are crucial in our day-to-day operations so we must make sure to have them working properly. The last one is just to save us time of having to import over every employee manually.
