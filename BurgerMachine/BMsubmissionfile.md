<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 5/3/2023 3:15:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236007753-097c0599-fd3e-4dc4-947d-cdfc779278e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot(s) of the updated method calculate_cost()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>If the value of &quot;inprogress_burger&quot; is false, then the output of the <br>&quot;calculate_cost&quot;<br>function would be zero. Otherwise, the function would <br>calculate the total price of<br>the burger by adding the individual prices <br>of its ingredients. The total price<br>would then be displayed in the <br>currency format by converting the &quot;anticipated&quot; variable,<br>which stores <br>the total price with a &quot;$&quot; symbol, into a float with<br>two decimal points.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236009287-4bc970a6-62d4-482e-b7c4-992bf25c2bfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> OutOfStockException is handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236010061-7d80bc4b-4669-434b-943a-db925ecb982d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException is handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236010968-d1ef6f39-5448-42bf-bb40-8cdf47f31cc8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceExceptions are handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236011208-71c3e1d8-a9ca-4665-90aa-736b95ff7307.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesExceptions are handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236011500-58dc9c67-1e99-4e69-ba44-d122b7e207e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException is handled <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>This code has several exception<br>handlers: OutOfStockException, NeedsCleaningException, InvalidChoiceException, ExceededRemainingChoiceException, and InvalidPaymentException. The OutOfStockException is raised when an<br>item is out of stock, the NeedsCleaningException is raised when machine needs cleaning,<br>the InvalidChoiceException is raised when the user enters an invalid option, the ExceededRemainingChoiceException<br>is raised when the user picks more than three burger or topping options,<br>and the InvalidPaymentException is raised when the user enters an improper currency format.</p></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236014191-2953bdb7-b807-4c2b-9d0e-5f1f73b16fa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236014631-f759b0c7-7364-41a0-9543-2afb0438315d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236014927-54d170df-442c-42c4-ac83-07b2cf5e4b44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236015113-f5aae644-6227-4902-9ff8-376c71f8651a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236015301-8efb86ca-f09f-4c56-9f49-463d82e123fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236015477-2d1e5f4c-1e7a-4f0e-a81f-20a390ed57b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236015773-60ff4494-f53d-43b0-b3b9-38edb9615547.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236016056-4a5bb8a4-8993-4274-9676-c2cf5fcead41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Case 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236020604-661236af-4baa-4bb2-bb95-86e4f8f75b2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tests 1-8 passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start gap-4 whitespace-pre-wrap break-words"><div class="markdown<br>prose w-full break-words dark:prose-invert light"><p>Response: test-1: We will check if selecting the patty<br>without bread will throw an InvalidStageException.</p><p>Test 2: We will reduce the turkey supply<br>to zero and test if it raises an OutOfStockException for that item.</p><p>Test 3:<br>We will set the quantity of lettuce to zero to see if it<br>raises an OutOfStockException for that item.</p><p>Test 4:&nbsp;we'll see if an ExceededRemainingChoicesException is thrown<br>if <br>the user chooses more than three patties from a variety of <br>available<br>options.</p><p>Test 5: We will test if choosing more than three toppings results in<br>an ExceededRemainingChoicesException.</p><p>Test 6: We will compare the actual cost of the burger to<br>the calculated cost from the calculate cost of burger function, including the "$"<br>symbol and a float value with two decimal places as the currency format<br>check.</p><p>Test 7: We will sum up the prices of three different burgers and<br>then execute an assert on that total.</p><p>Test 8: We will assert the total<br>number of burgers ordered.</p></div></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/29">https://github.com/VinoliaBattiri/IS601-006/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Faced issues with pytest connection and also got pip issues<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236019394-fdf75e06-164a-4287-8a60-22bfd642cce0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vb437" target="_blank">Grading</a></td></tr></table>