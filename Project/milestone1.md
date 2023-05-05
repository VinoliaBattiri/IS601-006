<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 4:54:58 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236552115-27c66244-d1b0-4d86-853c-97c915dc0375.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236552394-37f702df-6f23-49fc-93f2-cb0e05ae96ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236552679-65112b94-f89f-4f37-9ea8-54f08824cef8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not much validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236553207-28ecf1fa-f319-433a-8986-1a981808f9b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236553552-cb472ae8-c8a4-4baf-9032-4ddec2f5f7b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236554183-42322d48-f52b-4ff5-b1d2-5bb60c54489a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the form with valid data filled in before the form is submitted <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236554340-f5092ab7-17ed-470b-9936-ce1c04cf6567.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message after registration<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236554741-3ba848d2-1b57-4434-b6ae-ed6934d70ccf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 that is present in this screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>We use WT-forms to generate and validate forms. After submitting the <br>form, data<br>is delivered to our Python POST route, where it is extracted <br>and an<br>insert query is run to add the data to our sample table. The<br>data<br> is validated both on the frontend and backend using WT-form validators.<br> For<br>example, the username must be between 2 and 30 characters long and <br>not<br>have been used previously by another user, while the email address <br>is validated<br>using an email validator. The password and confirm password<br> fields should be identical<br>and have a minimum length of 8 characters. <br>WT-form validators are used to<br>validate these fields, and the hashed <br>password is stored in the database using<br>the bcrypt hashing algorithm. <br>The email address, username, and hashed password are stored<br>in the users<br> table.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236555508-a626dfea-0e0c-48b1-a1bd-2ebcdf24031c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236555797-d867e692-1a1e-40b1-b630-cc6851137507.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236556330-48ec1e94-70e3-4f25-aa28-cd00b6a30bb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>We used WT-forms to handle<br>the login form, which is similar to how we handle registration forms. However,<br>in the login form, we use the username or email field instead of<br>the confirm password field.</p><p>On the frontend, if the username or email field is<br>filled, it checks whether the entered data is valid or not. If the<br>entered data has the &quot;@&quot; symbol, then an email validator is used. Otherwise,<br>it checks whether the username format is correct or not, if the length<br>is between 2 and 30 or not, and if the password is entered<br>or not.</p><p>On the backend, we fetch the data from the users table by<br>passing the email/username. If the data exists, we compare the entered password and<br>check if the user is assigned any roles.</p><p>On the frontend, we first check<br>if the password is entered, and then in the backend, we fetch the<br>password from the database based on the username/email and check if the passwords<br>match. If they match, we delete the password from that point in the<br>program.</p><p>We fetch the username, email, and password from the users table by passing<br>the username/email, and then check if the passwords match. Then, we check if<br>the user is assigned any roles from the userroles table and fetch them.</p></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236559011-d14d4ef3-41d2-4656-bdca-06b5cc4cb43e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236559320-56268ff2-d11c-41f9-9e0a-3772a99395de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>we are using the Flask-Login package to manage and work with user <br>sessions.<br>In the main.py file, we define a LoginManager variable outside<br> of the factory<br>function, and inside the factory, we associate the app <br>with the LoginManager using<br>its init_app() method. To lookup a user by <br>ID, we use the user_loader<br>decorator inside the factory function.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236559320-56268ff2-d11c-41f9-9e0a-3772a99395de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236561869-17d99f5e-194b-4b8a-8d8e-f71b28950ad2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not having proper role or permission <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236562191-cd645252-7845-4204-89bf-898ba4c8e7d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data having at least one valid<br>record from the lessons (i.e., Admin) <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236562556-57a2959a-3435-47ba-846e-a43136b541cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the UserRoles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;we use the @admin_permission_require decorator function from the <br>roles.permissions package. If a user<br>attempts to access a role-protected<br> page without proper admin permissions, we raise a<br>403 exception and <br>display a 403 HTML page that says &quot;permission denied&quot;.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>This is similar to how we handle login-protected pages, where we use the<br><br>@login_required decorator function and call the <br>LoginManager.unauthorized function if the user is not<br>logged in. In both<br> cases, we define a variable for login_manager or <br>admin_permission_require<br>outside of the app factory and use its <br>associated init_app() method inside the<br>factory to associate the app<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236563253-86fe7d5d-2329-443e-839a-b2c652434c18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing Navigation bar with basic styles and with a clean UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236563466-e6eb8785-b8a6-4952-b27e-d9416ebdf327.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a forms which represents the profile page of the user/admin and<br>with a clean UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236563726-9b4e0e00-978e-4cef-b689-d8cef5b1873d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output of sample lists and with a clean UI<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>At a high level, the CSS used in this project utilizes Bootstrap to<br><br>create a responsive navigation bar that can be expanded or collapsed <br>based on<br>the screen size. The .navbar class is used to create the <br>standard navigation<br>bar, and the navbar-collapse class is used to group <br>and hide its contents.<br>The navbar-brand class is used for the company, <br>product, or project name, and<br>the navbar-toggler class is used to toggle<br> the navigation. The nav-item class is<br>used to change between different <br>types of navigation in the Bootstrap system. Additionally,<br>containers <br>are used as building blocks to contain, pad, and align content within<br>a <br>given device or viewport.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236559320-56268ff2-d11c-41f9-9e0a-3772a99395de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not being logged in <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236561869-17d99f5e-194b-4b8a-8d8e-f71b28950ad2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about not having proper role or permission (i.e., different than<br>the<br>not logged in message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236555508-a626dfea-0e0c-48b1-a1bd-2ebcdf24031c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash error pop ups when entered wrong password<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>To improve handling of access<br>denied and page not found errors, two functions have been created in main.py<br>that return render_template() for their respective error pages. These error pages have identical<br>user-friendly messages and can be customized as desired. The primary goal of this<br>is to enable users to easily navigate to the appropriate location with the<br>help of the navigation bar. Additionally, flash messages are included to guide users<br>on where they went wrong and help them correct any errors.</p></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236554183-42322d48-f52b-4ff5-b1d2-5bb60c54489a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user profile page where Email and username are properly prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp; &nbsp;when profile page is opened, if it is not a POST request<br>then email, username are fetched from users table passing user id, then the<br>are rendered into the profile form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236565302-9dc8d961-f89d-40f1-845a-e9082471046b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing password changed message which tells that password is validated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236565552-f249e95d-ab7a-40ba-ba72-c84699f1131e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing username changed message which tells that username validated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236566014-adc2a550-3c81-48f0-af8e-7b7b3e1380f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email changed message which tells that email validated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236566014-adc2a550-3c81-48f0-af8e-7b7b3e1380f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing email already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236566233-5d3a8986-b063-48da-9208-23fa9a1d4d7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236566451-6668ad48-8a32-4bf1-8ee2-0eae64eaa705.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user2 before edit in 4th place<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236566725-2faeab53-3539-4b63-9cd0-1ac76d645d34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user2 after editing in the 4th place <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/35">https://github.com/VinoliaBattiri/IS601-006/pull/35</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The code initially verifies whether the request is a POST request or <br>not.<br>If it is, it checks whether current_password, password, and confirm<br> fields are provided.<br>Next, it retrieves the password from the users <br>table and compares the current<br>password and the password from the <br>database to check if they are the<br>same. If they are not the same, it <br>will raise an invalid password<br>flask error. Otherwise, the new password <br>is hashed and updated in the database.<br>Finally, the username and email <br>are updated in the database, and a flash<br>message &quot;saved profile&quot; is <br>displayed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>I had the opportunity to<br>learn about user login sessions, registration and authentication systems, as well as integrating<br>database utilities to manage website data.</p></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finpro-prod.herokuapp.com/login">https://is601-vb437-finpro-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vb437" target="_blank">Grading</a></td></tr></table>