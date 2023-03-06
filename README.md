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


### Signing up

 
### Logout and login


### When the user is logged in 

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
 
 
### Remaining Bugs


### Validator Testing


## Deployment
This project was deployed early using Code Institute's mock terminal for Heroku
 #### Steps for early deployment:
  * Start by making a database using ElephantSQL. 
  * Then create a new Heroku app. 
  * Click on settings and Go to Convig Vars
  * Set Key to Port and Value to 8000. 
  * Then add my SECRET_KEY - same SECRET_KEY used on env.py
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
