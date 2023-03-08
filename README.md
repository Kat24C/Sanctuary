# Beloved Pet Sanctuary
Sanctuary is a place to help pets, which uses the Code Institute mock terminal on Heroku to run. 

Users can help by donating towards pets. They can fill out a form to adopt a pet and describe
what type of pet they are looking for.

https://animal-sanctuary.herokuapp.com/

<img src="https://user-images.githubusercontent.com/98415901/223212804-fc436b06-0840-4a50-a8a8-d38cd3bb94f3.JPG" width=50% alt="responsive design">

### User stories
 * The staff/superusers will be able to update the mission statement and how can you help statements. 
 * The staff/superusers will be able to add, update and delete animals as they need adopting or have been adopted.
 * The user will be able to go through the different animals and decide if they want to adopt an animal.
 * The user will be able to fill out a form stating if they want to adopt an animal.
 * The user will be able to search through the different animals using the search bar.
 * The user will be able to update and change their profiles as they are needed. 
 * The user will be able to donate a set amount to the cause to help. 
 * The user will be able to sign up for a monthly news letter.


## How to use the app
### Before login
 * The user will be able to click on links to get to the animal and about pages. 
 <img src="https://user-images.githubusercontent.com/98415901/223218511-bed34c7e-0dee-4703-901d-31d6f00dc3d5.JPG" width=50% alt="Home page">
 * The user will be able search for and look at all the animals.
 <img src="https://user-images.githubusercontent.com/98415901/223218009-fab22264-c432-4182-92dc-d037687bdf0f.JPG" width=50% alt="Image of the animals page">
 * The user will be able to read the mission statements and how can you help statements
 * The user will be able to donate a choosen amount by pressing on the link.
<img src="https://user-images.githubusercontent.com/98415901/223218621-d4c29ec5-33c9-42fe-9adf-745c7e2b19d0.JPG" width=50% alt="Image of the animals page">
<img src="https://user-images.githubusercontent.com/98415901/223218766-a15ce38c-7d07-4379-bf7b-b9391db2c5cf.JPG" width=50% alt="Image of the animals page">
 * Once the user has made a payment they will get a thank you note.
<img src="https://user-images.githubusercontent.com/98415901/223218900-f17e350c-a2ac-4e6f-8c51-e10346a58512.JPG" width=50% alt="Image of the animals page">
 * The user will be able to click on the animals to find out more information
 <img src="https://user-images.githubusercontent.com/98415901/223218086-46e80fe7-91aa-45cf-a288-5d8985aa36ef.JPG" width=50% alt="Facebook page">

### Signing up, login, logout
 * The user is able to go to the sign up form, login and logout by going to Profile in the nav link. 
<img src="https://user-images.githubusercontent.com/98415901/223219808-5c559700-00f2-47f5-b0fe-1d36fe0e6206.JPG" width=50% alt="Facebook page">

### When the user is logged in 
 * The user is able to fill out and update their profile. 
 * The user will be able to send and adoptiong form email.

<img src="https://user-images.githubusercontent.com/98415901/223216941-8b73df80-a57e-455a-bad4-f6f7b0c4be43.jpg" width=50% alt="Facebook page">
<img src="https://user-images.githubusercontent.com/98415901/223220097-e538c814-a6e3-4e17-8ead-399514ff02fb.JPG" width=50% alt="Email form">


### Facebook page
 * I used a mockup facebook page to show an example of the facebook page. I used krita to design it. 

<img src="https://user-images.githubusercontent.com/98415901/223216941-8b73df80-a57e-455a-bad4-f6f7b0c4be43.jpg" width=50% alt="Facebook page">

### Mailchimp
 * Used pop up link to link mailchimp to the website.
<img src="https://user-images.githubusercontent.com/98415901/223217264-629c6298-167b-48eb-a0e5-36920065b4e4.JPG" width=50% alt="Facebook page">

<img src="https://user-images.githubusercontent.com/98415901/223217350-757aec05-cae1-4d44-a292-2669729e9685.JPG" width=50% alt="Facebook page">

## Features

 ## Testing
 
 ### User story testing
 * The staff/superusers are able to update the mission statement and how can you help statements by logging in and clicking on the edit the statement link, which will take them to a new page where they can update the user story. 
 * The staff/superusers are able to add a new animal by going to the add me link in animals, update the animals by clicking on the know more link where they will then find a edit or delete button, which will take them to another page..
 * The user are able to go through the different animals and decide if they want to adopt an animal by clicking on the animal link.
 * The user are able to fill out a form stating if they want to adopt an animal, by clicking on the adoption link, logging in and filling out the form. This will send an email to the staff members.
 * The user are able to search through the different animals using the search bar at the top in the navbar.
 * The user are able to update and change their profiles by logging in clicking on profile and updating what is needed, then clicking Update Information to save the changes. 
 * The users are able to donate a set amount by clicking on donation and choosing what they want to donate. This will then take them to another page where they can fill in their card details, if successful it takes them to a thank you page. 
 * The user are able to sign up for a monthly news letter by clicking on the pop up and filling in their email.



## Bugs
### Solved Bugs
 * When searching for a type of animal it was not working. 
   * I fixed this by adding a search_animals views and url for search_animals.
 * When paying for a donation, the previous payment stayed in the bag/ 
   * I fixed this by adding: if 'bag' in request.session:
         del request.session['bag']
 * When signing up, there was a 500 error.
   * This was fixed by removing the phone_number link in profile as it was picking up 2 number. 
 * My custom 404 was not being picked up. 
   * This was fixed by removing the url and view handler and adding the 404.html to base template instead of the root directory.
 
### Remaining Bugs
 * There are no remaining bugs. 

### Validator Testing
 * By running my project through lighthouse in devtool, I confirmed that the colours and fonts are easy to read and accessible. 
 * CSS
   * No errors were found when running the css code through jigsaw W3C code validator
 * HTML
   * No errors were found when running the html code through validator W3
* Python
  * Ran linter in gitpod, had 2 long lines in settings which were imported when I installed django. 
  * Ran automated testing using tests.py = test_models
* Accessibility
  * By running my project through lighthouse in devtool, I confirmed that the colours and fonts are easy to read and accessible. 


## Deployment
This project was deployed early using Code Institute's mock terminal for Heroku
 #### Steps for early deployment:
  * Start by making a database using ElephantSQL. 
  * Then create a new Heroku app. 
  * Click on settings and Go to Convig Vars
  * Set Key to Port and Value to 8000. 
  * Then add my SECRET_KEY - same SECRET_KEY used on env.py
  * Add Stripe_secret_key and stripe_public_key to convig vars.
  * Then add DISABLE_COLLECTSTATIC for early deployment
  * Click on Deploy at top of page. 
  * Change Deployment method to GitHub. 
  * Connect to GitHub and add repository recipe. 
  * Check if manual deploy is on main otherwise set to main. 
  * Click on Deploy Branch
 #### Steps for final deployment:
  * Change Debug to False
  * git add . git commit -m and git push your code to github
  * Click on settings and Go to Convig Vars
  * Remove Disable_collectstatic
  * Go to Deploy at the top of your page. 
  * Once in Deploy go to the bottom and click on Deploy Branch. 
  * View you build log. 
  * Once the app has launched wait 30 seconds and open your app. 

## Credits
 * Code institute for the deployment terminal
 * Code institute Hello Django and Boutique Ado. 
 * https://docs.djangoproject.com
 * https://ordinarycoders.com/blog/article/django-messages-framework
 * https://learn.microsoft.com/en-us/aspnet/web-api/overview/testing-and-debugging/unit-testing-controllers-in-web-api
 * https://docs.djangoproject.com
 * https://learn.microsoft.com/en-us/aspnet/web-api/overview/testing-and-debugging/unit-testing-controllers-in-web-api
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
 * https://getbootstrap.com/docs/5.2/getting-started/introduction/
 * Dom Vacchiano - Django tutorial for beginners/Django full stack
 * Images from https://unsplash.com/, pixabay.com, stock.adobe.com
 * Slackoverflow for css animation of messages
 * Followed clevertechie to update navbar. 
 * Used django-phonenumber-field.readthedocs.io
 * For stripe payment I followed dennis Ivy, Boutique Ado, Pretty Printed and Django road.
 * Codemy - Create a search bar.
