<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vinolia Battiri (vb437)</td></tr>
<tr><td> <em>Generated: </em> 5/6/2023 5:47:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vb437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646158-315a4548-20d8-4e5d-a22e-844f418577d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin create page with a valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646210-10852102-b790-43b2-bd38-ffffc2df52dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all the products and the latest added product is highlighted in<br>the last<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>When the user enters values on the add page, they are sent to<br>the item <br>function in shop.py. To distinguish between adding a new item or<br>editing<br> an existing one, the code checks if an id has been passed.<br>If no id is <br>supplied, a new item is created using an INSERT<br>statement and the values<br> are passed to the Products table. If the operation<br>is successful, a <br>flash message is displayed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646368-73e70da2-3ae7-4bce-b471-83db98622045.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646453-aa33c983-0dff-4c2b-8158-297dde0acd14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646483-de399307-7b30-4da8-aad6-1494110219d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filter with Electronics and sorted from<br>low to high price<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646501-39f0ca82-5df4-40e1-9372-219ef10a3afa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filter with food and sorted from<br>high to low<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646550-9c0999b0-cd3e-4856-b478-e598d4f54dc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>The Products table with visibility set to 1 provides the initial data <br>for<br>the shop page. Additionally, the page allows for searching by name, <br>selecting categories,<br>and sorting prices from &quot;High to Low&quot; or &quot;Low to <br>High&quot;. If one<br>or more of these search options are used, the shop.py <br>function&#39;s shop list<br>is called and the query&#39;s where condition is <br>modified based on the input,<br>and the results are displayed again.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646593-baa6093a-98fa-4372-88c7-71baf4eb917e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>Without applying any filters, we choose every field from the Products database and<br>feed it to the HTML page. Since no conditions are stated anywhere, every<br>product will be shown regardless of visibility&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646647-6debb79e-299a-411d-86c7-acf01ef65936.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646687-fab3f7f1-e081-40d1-af2b-575b9b5a0d85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646593-baa6093a-98fa-4372-88c7-71baf4eb917e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page  (The admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646730-6efdbf8d-434b-4058-bd44-06e717058dab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit page with present details of the product Dark Chocolate<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646880-1dec61c6-92e8-4c1a-ac94-5cccf260fd5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products before editing the product Dark Chocolate<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236646956-5103b5bc-73fe-4f9e-b87c-8d91362f1557.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit page with changed details of the product Dark Chocolate<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647016-326f013c-97c0-4fa1-a506-5d4e7e73e82b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products after editing the product Dark Chocolate<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>In the shop page, for each product, there is a check to verify<br>if the <br>user is an admin and logged in. If both conditions are<br>met, an edit <br>button will be displayed which redirects the user to the<br>item page with <br>the product details. Similarly, on the item details page, the<br>edit <br>button will be displayed for admins only. On the admin items page,<br>the <br>edit button is displayed by default since only administrators can access<br> the<br>page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647085-94bc60d7-0960-45ba-911f-fa7bf4c1ed07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page Checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647131-34b2bf58-475b-4986-ab09-dbe54d5ec91b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the result of the Product Hoodie<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>I created the itemdetails.html file<br>and implemented the item details function. On the shop page, the product name<br>is now a clickable link that sends the product ID to the item<br>details function. This function retrieves all the relevant product information from the Products<br>database using the ID and displays it on the item details page.</p></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647169-f4115a9d-0b5c-41b4-ba37-222064adddf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding product Hoodie<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647206-d8342c2b-d8fc-427b-b236-cc5d8e1d988b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart when not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647275-27b2c053-fc7d-4c75-9292-7886afec6107.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>The cart system allows for one cart per user, with a composite unique<br><br>key of product id and user id. When a user adds a product<br>to their cart,<br> the system performs an insert query to add the data<br>to the cart table <br>in the database. Similarly, when a user wants to<br>update the quantity or <br>remove a product from their cart, the system performs<br>update and delete <br>queries accordingly. The products in the cart are retrieved from<br>the <br>shop and added to the user&#39;s cart as needed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>The cart function in shop.py<br>receives the product id as a hidden field and the amount field when<br>the ADD button is clicked. If the quantity is greater than 0, the<br>product id, user id, desired quantity, and unit price (which is obtained from<br>the products table) are inserted into the database.</p></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647311-7b39c3ff-815f-4eea-ab47-32ef85e72b0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View with subtotal of each line and adding up,<br>cart total,  link to product details page for each product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p><text x="-9999" y="-9999"></text><span class="flex-grow flex-shrink-0"></span><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start<br>gap-4 whitespace-pre-wrap break-words"><div class="markdown prose w-full break-words dark:prose-invert light"><p>When the cart is clicked,<br>the function checks whether a product ID is passed or not. If not,<br>it goes to the SELECT block to retrieve the user ID, product ID,<br>name, desired quantity, and unit price, calculates the subtotal by multiplying the desired<br>quantity by the unit price, and sends these values to cart.html. The items<br>are rendered as rows in a table in the HTML output to calculate<br>the total. The subtotal value for each row is added to a variable<br>called &quot;ns.total,&quot; which is displayed at the bottom.</p></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647365-b68ba2b9-0503-46dd-87ff-6546b49364b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing before updating the quantity of product Bread<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647389-110726f3-787b-4ce9-9e0d-884616fbae21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after updating the quantity of product Bread<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647510-d1f9db5a-8cfa-4ae4-8042-414572d846ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart before setting the quantity to 0 for product Hoodie<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647544-c92537a2-c7bf-42fb-a216-93568b999e2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the product hoodie editing as items in cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647578-ad4047ad-2fb0-4a48-9f68-312ee98f7632.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart after setting the quantity to 0 for product Hoodie<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647423-d6fce3d0-ce75-4b34-b3ea-b2ed6642bb88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing how a negative quantity is handled when tried to set -1 to<br>the product &quot;Beef Jerky&quot;	<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>To update the cart in the shopping cart feature, a hidden product id<br>is <br>sent to the cart function when the user clicks the update button<br>next to<br> the amount field. If the quantity is greater than 0, the<br>function <br>retrieves the name and price from the products table and updates the<br><br>quantity and price in the cart table using the product id and user<br>id. <br>If the quantity is less than or equal to 0, the code<br>moves to the DELETE<br> block, where the product is removed from the cart<br>database by passing <br>the product id and user id. To handle negative values<br>in the amount <br>field, the minimum value for the input field in HTML<br>is set to 0.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647737-3011edcb-a4a9-4798-a4ff-fbded6e2be33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart before deleting the product cheese from the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647761-4e964491-8371-4d0f-bf42-a7d56c1ee53a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart after deleting the product cheese from the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647640-dc1b312e-b2c9-4428-b09e-857d2a5e26e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing before clearing a cart completely<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420587/236647658-c0b4d4f7-4862-407b-a500-6d230877285d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after the clearing the cart completely<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>To delete a single item from a cart, the delete button is accompanied<br>by<br> a hidden field containing the value of -1. The cart function processes<br><br>the delete query and sends the product id if the value is less<br>than <br>zero. When clearing the entire cart, the variable &quot;delete all&quot; is passed<br><br>with a value of 1. If the value of &quot;delete all&quot; is True<br>in the cart <br>method, the records in the Cart table are deleted while<br>passing the user<br> id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/VinoliaBattiri/IS601-006/pull/37">https://github.com/VinoliaBattiri/IS601-006/pull/37</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I encountered a problem while creating tables because the cart table <br>depends on<br>the product table, but the query for creating the cart table <br>was executed<br>before the product table was created. As a result, the <br>product table was<br>created, but the items couldn&#39;t be added to the cart. I<br> eventually realized<br>that the cart table wasn&#39;t created at all and had <br>to run the<br>inti_db.py script again to create it. Despite this issue, I <br>was able to<br>learn how to build webpages in a real-life project.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vb437-finalproject-prod.herokuapp.com/">https://is601-vb437-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vb437" target="_blank">Grading</a></td></tr></table>

