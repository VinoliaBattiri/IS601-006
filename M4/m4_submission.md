<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2023 1:26:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235734360-77f86203-0e8c-41d2-8483-d0cc9f01e04c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>addition function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235734653-2dc0f91d-8270-46ee-8dd7-1b5c732f023a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235734909-80541863-c74c-42e2-a07d-df75ce641c2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235735165-0e520028-3411-4781-a3d9-f1ee017ffded.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>division Function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736331-5faa4d00-4bda-44ad-9a22-7669b27e6943.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-add-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736968-306adc88-ed30-4ed4-b51b-0d8bfb1a76c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-add-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235737183-edbabc1d-3d1a-49c5-911b-0eb8b12f5495.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> number-sub-number Test<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235737454-155fd0ee-00e3-4cbf-b71d-7a92fb0d4f9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-sub-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235737706-1c6f08d0-81cc-4678-9baa-0464aab59ba2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235737918-c4c4d73c-1981-49f9-ad82-6b695afb4ea9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235738194-18693141-1349-4613-a867-0e856406528d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235738437-8b0c34e8-57ab-4683-ae96-4eabb74839ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number Test Case <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/235736471-5a5fc9c8-651a-421a-be0e-9a13d3724f12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing in pytest<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>learnt how to use pytest and running the test cases<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>learnt how to use pytest and running the test cases.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/17">https://github.com/VinoliaBattiri/IS601-006/pull/17</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/vb437" target="_blank">Grading</a></td></tr></table>