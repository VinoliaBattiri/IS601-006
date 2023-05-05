<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 5/4/2023 7:30:59 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236332164-2f9acfcb-d70d-4ff6-8e74-004c84c584b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236332525-78148e9c-4e5a-4fcf-b3aa-4a662575efdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Tables from VS code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236332998-5385cc8d-caae-4c80-b6ed-fc86bbbc297d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checking whether the file is .csv or not:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236333294-fca063da-1656-4261-8a39-8334792a2356.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code reading file and appending into dictonary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236333560-560c98dd-9d84-4597-9df0-c1c9db7fdfb3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of processed records showing in flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236333869-e190b34a-825b-48a4-92fe-cbc80f7cfb9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code if nothing was loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236334253-56ed4d9c-7d51-4da1-aabf-680669225524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import successful and Count of records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236334427-a5b62f36-38cd-4647-be22-3c058c9e571c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid file message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236334638-fc720c76-4ded-4850-9b10-5c8c83a43cf3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if submitted without attachment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236334893-a7708e90-000b-4172-be31-58006f0d39c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employees data in table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236335085-4411bbb2-1bbe-4b10-8073-b1d1aa9551c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Companies data in table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236335369-572bd6db-c876-49e3-bac3-5ced644bf8d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retrieving first_name, last_name, company (id), email with flash messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236335547-c2b4be18-f48e-41b6-808d-8e20f70e5341.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert query and flash message to print exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236335887-6bb937ba-eff6-42c2-8f01-6d1dcd3bd5e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if submitted without filling<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236336106-8a53d2b2-02c8-435e-bfec-4065447c3923.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236336295-9b8144a2-4e0d-433f-87ae-52d4fdf53e73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236336454-1d864105-b500-40ee-8b97-009afab12e4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236336682-3bd49f78-b751-491d-bdc2-515dea7d9df1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337006-3bad57bc-14b6-4095-8e55-5249153ff6c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Employee record data - Vinolia Battiri<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337394-15cfe3f8-ccdf-421c-85ea-bcab2f8487b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select query to retrive data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337526-df9c26b3-9913-4928-9bee-eb719692514e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking requested args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337676-208407b0-3845-4609-93a5-bc13d84fe881.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Appending like filter for First_name,last_name,email,company_id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337813-5ec7a1a4-8882-44fd-935f-e6e3505a3947.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append sorting allowed columns<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236337954-9c676c75-1187-4a63-b343-916d3b68b187.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message if limit is out of bond<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236338105-a728d134-6e92-4b2b-b4e1-1675d9692374.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception handling message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236338377-1a9529a6-3b4c-4b44-bbbb-f7f6656d2e8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236338256-09e67c00-a78d-4bae-a5a4-027a76cf7d71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236338718-b9cf2aa6-15fa-4930-aede-cbaf1de77687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236338813-eaa8b5fa-b7c2-469a-ad7c-be5220a018f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236339002-cc19dbfa-aefa-4524-bf38-974064537303.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with asc order filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236339132-08dab127-ac92-4687-a945-5477fd72f072.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with desc order filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340044-3a6fcd7b-7bdb-4b3a-b712-9be5b7c4ae21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form. Missing id should be handled with a flash message and redirected back<br>to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340245-e3d4f665-3999-4097-b72e-fec60f54251c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message first_name, last_name, email, company(not required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340467-2016c235-579a-43c4-a853-e0d0bf250d81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340559-17c8af97-b39c-4ccf-8c81-5f3ad21a3ee1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (two) should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340708-23593e36-6d3a-46af-84dc-e6624362914c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340782-4ddb35b1-f519-4c7e-95dc-1425866f85fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236340912-9acca321-7f8d-4b84-8c84-1e2965b352ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236341751-098b4060-8733-41d8-806c-4ff4e7a62962.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236343164-005eb40d-488b-41f9-b47b-2122240b5e4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236343072-3c349178-435d-44e6-8b04-2a5c1f3176ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>editing last name (garisa-Nagisetty) , Company (no company-c4 network inc)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236343363-ea91c3ba-18c5-429a-bcc4-05960241c07b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieve form data for name, address, city, state, country, zip, website and<br>flash<br>messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236343475-8f697e43-c69b-4e3e-a2ee-15cd1e202b7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236343594-54298ba0-c338-4c28-9b21-480df1124bf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user-friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344046-f2209ea9-68f0-441b-899b-2ba2d2dfe841.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344223-d6644d6c-8f07-477b-b9dd-b10d855eb28e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message for company name, address, city, zip code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344466-eea136c7-d63b-4e10-b97f-7ce452100a2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message, if country is missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344538-66c3e9f2-5734-48b3-929d-1c94962bf1b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if state is missing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344657-438204b2-bc4b-4535-8368-87b2645dbace.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid company data shown previously (NJIT- last one id=45)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344849-0b4178c6-5613-4589-86c1-420ac9239154.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count<br>(as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236344996-508dd21b-5f21-401d-9c80-e6339cfd4739.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345126-c93a76c3-e8fb-4e6e-b792-e97d51cb1a58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append an equality filter for state if provided,if country provided and name:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345233-122d3668-82b8-46e3-aece-0054d09eb06e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [name, city, country, state]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345489-103361f1-e387-4650-a833-84fc19170d0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100 and printing error message if it exceeds:<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345716-80ca689d-3a10-4f01-bee8-a3a164eefb1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345831-7f31dc49-d71c-4d30-9d49-d8097ab3411c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236345931-8df1d805-2c41-4ed2-8a1d-7eca9c79e120.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236346075-50242ed2-77f8-4cae-a8c8-5f0f820fe601.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236346321-c9c2ea35-2ec3-4614-ab49-d930f3c50150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen) - Name<br>column:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236346793-c333b308-e27c-4431-a03f-533f00c7f83d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen) - Name<br>column<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347355-faca1e73-8be2-45ee-99ac-4a90ae5fdbb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form. If id is present flash related error message and redirect<br>to<br>company search and flash messages if they are missing:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347483-598f620a-dba4-40c6-a9f9-3fc18e5b79c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347594-128c6fc2-47cf-4674-843c-f052c98ae9ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible with the passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347707-766bb127-045a-4a78-bc66-8e6ff08658c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347802-a42bd4d2-b5d1-435f-b7d0-a190ee2a356e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236347802-a42bd4d2-b5d1-435f-b7d0-a190ee2a356e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit - Name (NJIT- NJIT education), address (passaic ave- passaic ave 1),city<br>(Newark-New jersey)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348187-607ec617-061c-4b69-84b2-33aa8b8d4693.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before edit in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348322-a63e5619-f995-4b68-a584-b45699fb75d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit in database- Name (NJIT- NJIT education), address (passaic ave- passaic ave<br>1),city (Newark-New jersey):<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348455-264c5c71-16e6-4436-bc0e-a6eef3035823.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete employee by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348538-ba02e874-6735-4d28-846b-b690c73dfd07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348658-a9743274-c38a-4395-8ab5-98be4ac70afe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route and success<br>flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348804-75701aa2-d7a4-4807-865a-1a19c64d287f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting employee data in database:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348804-75701aa2-d7a4-4807-865a-1a19c64d287f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting employee data in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236348992-27d0cc98-795a-413c-be4b-b83c51b16eca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349154-0244d4b4-e332-483f-a837-e4ad2fd81bf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349238-0d95e711-6541-49da-a5a5-04f83ec7c9c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete company by id, if missing should flash the related message:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349315-24c534a4-c60c-43fb-8cdd-9da8afc8e52d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to company search:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349379-c4d79fe0-2528-4f67-8b7e-6481126a0f1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route and success<br>flash message:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349535-2b7a641c-d2ba-415c-9222-b3697ca8369d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company details in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349621-11bd87f2-6d04-46d9-ac43-b973733e72c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company details in database - NJIT EDUCATION(last)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349766-dc3c39ef-7813-47eb-b29c-130c8a988d94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company details in website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236349950-8deda76b-2fd0-4357-aeca-7d3475311253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_upload_csv.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350032-1e39f035-41b5-488c-b974-3addefe26e60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350116-1f523e2c-d00f-4b6f-89f3-42ee9d79a3cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350206-b862784e-22a5-4575-a00f-2b96d54163b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350286-6ff48e79-2583-40f8-bd16-810631ccb6ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350388-bc2a27e8-411f-4725-9945-2d1b9230c414.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236350493-7898c4f6-adb6-46b9-af5f-7e1768789370.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_employee.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Understood how we can use jinja templates and how flask can be used<br>as a best framework for python. Faced issues while running the requirements file<br>where I had to copy all the requirements again from the main folder<br>and had to run again.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vb437" target="_blank">Grading</a></td></tr></table>