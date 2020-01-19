### https://milestone-project-004.herokuapp.com/
 
## Milestone Project 4 (Paddy Boyle photography website for portfolio & shop)

### Initiation -

I have decided to develop a new website for my client Paddy boyle. This website will be in addition to the other website I built for him which encompassed his property photography Find it here https://milestone-project-003.herokuapp.com/. This new site will be to showcase all his other work and will have an online shop included that sells prints.

### Kickstarter Meeting -

After talking with Paddy, we decided on a few main points I found out that he needs different categories for his photo galleries, i.e:

* People
* Places
* Things

He would also like an about section, a prices section and a contact section. One of the main features will be an online shop with user authentication for the shopping basket and checkout. These users will be held in a database.

### Thoughts after the meeting:

I think that for the front end design, I should keep the layout that I used for his property photography site to keep consistency. I will change the colour from blue to green. He also wants it to be titled Paddy Boyle Photo Archive.
 
### Main Technology Requirements for Project -

#### Required:

* HTML & CSS:
I will be able to use bootstrap to structure and style the front end of the site. The home page, about section, services section, contact section and shop page should be easy enough to implement with this framework.

* Javascript:
Relevant Javascript could be used for lightbox galleries and the contact form.

* Python & Django:
I think categorized photo galleries would be a good way to implement Django templates with Python. Also a navbar template for every page on the site. The Django framework will allow me to create the 
shop application

* Relational Database 
I will use MySQL to store information about users that register and authenticate to the site so as to use the online shop. I will implement the Django admin interface to manipulate the data.

* Stripe Payments
I will use stripe payments to create the e-commerce section of the website.

* User Interaction
I will create a blog page for extra user form validation.
 
### User Stories

* As a user I want to understand what the website is for in an about section.
* As a user I want to be given a selection of images available to buy from online shop.
* As a user I want to have a shopping cart to see what I have selected to buy.
* As a user I want to log into my individual shopping cart.
* As a user I want a secure checkout when purchasing items.
* As a user I want to be able to easily find images the photographer has taken in a portfolio section.
* As a user I want to be able to easily navigate through the site using navigational links that are consistent throughout.
* As a user I want to be able to contact the site owner in a contact section.
* As a user I want to get an understanding of the Image size options that are available from the shop.
* As a user I want to have access to the site owners social media.
 
## Plan -

### Initial UX/UI Development -

#### Home Page 

I have had a research into contemporary photography websites and settled on a simple homepage design that shows a striking image provided by paddy. He will be providing all of the Images for this project. This image will be full width and height. 

#### Nav Bar

A nav bar across the top will be stuck to all pages as a template and also stuck as the user scrolls down the page. It will be fully responsive along with the rest of the site. The nave bar will encompass a logotype, the about section link, a portfolio section link, a prices section link and the contact section link.

#### About section

Here I will have paddy write a bio and description of his profession.

#### Category pages

With the use of the Django admin DBMS I will call data from the database to populate these photo galleries. A simple bootstrap gallery will suffice. I will format all the images so they are the same size which will make the layout easier to make responsive.

#### Prices and image size option section

I will use the information from the old site to populate this section in a three column grid. This will give the user a description of what is available from the shop

#### Contact section

I will use the gmail jsmail API to implement a contact form with a bootstrap themed form.
 
### Wireframe Sketches -

As this site is for the same client as my milestone three project I decided to use the same 'freelancer' template from https://startbootstrap.com/themes/ I kept this for brand architecture consistency. This would also allow me to save time and concentrate on the back end functionality. 

### GitHub Issue - 

Unfortunately I had an issue with the first 14 commits for my project. I accidentally tried to rewrite a model in my products app and when I migrated the changes I got an error I couldn’t get rid of. After a while I decided to start again from the last commit (the 14th). I think I may have done this wrong, I closed my text editor and deleted the directory. Then I downloaded the files from the most up to date commit. I set up my text editor and venv with these files and tried to reconnect to the remote repository. I had trouble with this and asked for tutor assistance. Unfortunately something went wrong and I ended up losing all my previous commits when I pushed the new files to the repository. After looking into what happened with the tutor team it seemed that when I copied the files over, it modified my git file/settings locally without letting me know.  This could have reset my Git Head and hard reset it. The conversation I had with one of the tutors is attached to my student profile so it can be referenced if needed for proof. Fortunately I had been documenting everything in writing as I went so I hope that this will make up for the loss of commits for the first half of the project This documentation is below.
 
## Documentation -

### Initial Setup and instalations

For this fourth and final project I decided to use visual studio code. I feel that even though in Code Institute we are advised to use GitPod as it is easier to screen share with tutors, It is less prone to unwanted surprises and lagging. I downloaded and installed anaconda, a powerful package manager and environment manager that you use with command line commands. 
Venv and First App Setup

Once installed I created and activated an environment called ‘milestone_env’. Then I created a project called ‘milestone_004’ I then ran the server to check everything was working ok. After this I created my first app called ‘app_001’, this will encompass the front end of the site. I went to settings.py and under INSTALLED APPS I input the ‘app_001’. 

### Testing ‘app_001’
Later I would set up templates with a base.html for all the urls but for now I just wanted to test that ‘app_001’ would link a index.html to the server. I created a template folder in the main project directory ‘milestone_004’ called ‘templates’ and then created a folder inside that called ‘app_001’ to hold ‘index.html’. This would link to a function in the views.py file which returns ‘Testing!’ to the server in the index.html page. Once I created this function I went to the main project urls.py and imported the ‘app_001 views and the url patterns for the index page. I then ran the server and the linkage was successful, I could see ‘Testing!” in the server. URL mapping linking an apps own url.py is better practise so I created a new urls.py in the app_001 directory and configured up all the url patterns this way.

### Template Tag Testing

To set up the template tag in index.html, I input some boilerplate code and inside the body tags I input the template tag {{ insert_content }}, then I went to views.py in the app_001 directory and created a new function called index that I could use to test all my mapping for this page so far. I then went to settings.py to configure the TEMPLATE_DIR. The test was successful, it showed “This is text from views.py” from the template tag key pair.
Base.html & Static folder

Once I completed the mapping for the front end functionality, I created a ‘base.html’ in the templates folder for template inheritance. In this I used the same bootstrap theme that I used for Paddys other site. This theme came with its own static files so I created a static folder in the main project file ‘milestone_004’ and placed them inside that. I then configured the static file settings in ‘settings.py’ once I had the base.html set up I can extend the layout to the index.html file. 

### CSS Styling

The only aesthetic changes my client wanted to make to the new sites layout was the colour of the sections and hovers. He decided on a light blue ‘#408be6’ I adjusted the css to make this change. While I am waiting for the gallery images and about section text, I thought it would be better to work on the user authentication.

### User Authentication

To start developing the user authentication I set up the hasher algorithm configuration in settings.py and then pip installed bycrypt and django[argon2]. Then I went to the models.py to set up the user model, I created a class called UserProfileInfo. I then created a forms.py file and made the form classes. After this I needed to register the model to the admin so when you log into the admin you can see the actual model. So in short I have created the UserProfilInfo model that is a OneToOne match to the built in user with django and made the forms that will collect information about the user from the registration page and the admin.py file. Next I connected these to the templates.

### Templates

I now created the registration.html and login.html and placed them both in the templates folder. In the registration file I created a form which connects to the context dictionaries that will run with the views.py file when I complete it. I also mapped out the url for the registration page app urls.py. I now created a ‘shop.html’ and the relative views.py function request. I also linked template tagging to shop.html and registration.html in urls.py.

In views,py I firstly created a function for the registration form on registration.html I thought it would be best to tidy up the css later once all the functionality was finished. Once It I finished coding it I ran the project in the browser and typed ‘app_001/registration/’ in the url after the port. The form showed up successfully and I entered some user info. The page took this info and returned a ‘Thanks for registering message’. I then created a super user and typed ‘/admin/’ into the url. I put in the super user username and password to check if the registration for was linking to the Django database successfully, and it was.

### App_001 (Views.py)

In the views.py I used ‘from django.contrib.auth.decorators import login_requerd’ to make sure the user is logged in to access a specific page. This import will help me write the function for the user login. I also added some other imports to develop the user login, these included: 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

### User Login

Next was to create the user_login function. This function will authenticate, then check if the user is active, if not it will log the user in and return to the index page. If the account is not active, an error message will appear “Your account is not active”. If a failed attempt happens the attempted username and password will be printed with “Invalid login details supplied”.
On the base.html nav bar I added an if statement that will change the navbar link text from log in to log out once the user has logged in using template tags. This also links to the user_logout function I created in the views.py file. To be able to log out the @login_required model will need to be used with the request which returns the user back to the index page changing the link back to login. 

### Online Shop

For the shop I created a new app, I had to use some tuition from code institute to complete this task as I was unsure about how to go about it. I made a product model in the relative models.py and added a name, description, price and image for each product. Then I registered this Product class to the admin. I then pip installed ‘pillow’ as this package is used to manipulate images from a database. I then made a function called all_products in views.py, this would point to the products.html (shop). I developed a products.html and extended the base_002.html (base_002.html has a different nav bar) and made a form and a for loop that would iterate through the the products that I add in the database. Then I mapped all the urls in both the products urls.py and the main projects urls.py. Once I had finished I ran the server and went to admin and made a product in the database. I went back to the products.html page and the product was displayed on the page.

### Shopping Cart

I used a similar process for the shopping cart I admit that I used the functions from code institute in the views.py using the DRY principle. The changes I made to the code included the @login_required, which only allows logged in users to view their shopping cart. When you hover over the logout navbar link a javascript alert states “Warning! All shopping cart data will be lost if you log out”. To allow the user to click on this link I needed to make an if statement that allows you to click it after the alert pop up has gone and so if you reload the page the alert will still appear if you hover. I restyled the products.html and cart.html so they were more consistent with the other counterpart site. 

### Portfolio Photography Showcase

For the portfolio showcase I created a new app called categories even though I did not have all the photos yer I could still create the galleries. Then I made four new models in this app: Catagory_001, Catagory_002, Catagory_003 and Catagory_004. These models had a name, image and url fields the url would be used to enlarge the gallery image when it is clicked on.  Then I added these model classes to the admin.py so they would link to the Django database. I then added the app to the settings.py under installed apps. After this I logged into the admin page to see if the databases had been created, and they had been. I used this same method to create all four categories.

### Extra Styling

Next I styled the login and registration pages so they were more consistent with the overall layout. I also fixed some issues with the responsive layout in the portfolio galleries. 

### Stripe Checkout

Next I developed the stripe ecommerce section. I firstly will pip install stripe in the terminal. Then I configured all the settings in settings.py, Then I created an app called checkout that I then made an Order class and an OrderLineItem class in models.py for the models. I registered these in the admin.py and migrated to the database. In the views I took some code from code institutes source material for a checkout function view request. Then the following urls.

### Testing Checkout

Now the checkout was finished I checked it with a test card. The transaction was accepted. 

### Images from Client

My client finally had formatted all the images for me to upload to the Django database. I firstly uploaded all the images to www.imgbb.com to generate individual urls for each image. I added a url requirement to the portfolio image model so when the user clicks on an image it becomes enlarged. 
I filled in the model requirements in the database, which include a name, a URL, and the image.jpg (which I compressed). Then all the individual category images are displayed in the relative html files using for loops. This is the same for the online shop.

### Setting up PostgreSQL database

From now on I have documented the steps I have taken but I have been following the Code Institute tutorials as this is my first time setting up AWS. 

In heroku I added on postgresql to the dashboard. In settings I copied the config variable URL and returned to my text editor. I installed dj-database-url and then downloaded homebrew to install postgresql.

### Configuring PostreSQL in settings.py

Now connected, I created a requirements.txt then went to settings.py and imported dj-database-url then reconfigured the DATABASES. I then added the Heroku config variable to the env.py. Then I migrated all existing migrations to the new postgresql database and created a new superuser.

### Setting Up AWS S3 Buckets

I already had an aws account that I logged into and then clicked on S3 on the dashboard. I went to create a new bucket and followed the steps on screen. Once the bucket was created I clicked on it and in properties I clicked on static web hosting. I saved the settings in this then went to permissions and then CORS configuration. I copied and pasted the CORS configuration from Code Institute and then the same for the bucket policy. I go to ‘Identity and Access Management’ to create a new group. to create a new policy I import s3 and input my arn. Once I have renewed the policy I add it to the group I previously made. I now create a user and download the csv file and put it in a folder for safe keeping on my desktop. I then test the bucket by uploading a random image.

### Adding S3 To Django

I already had an aws account that I logged into and then clicked on S3 on the dashboard. I went to create a new bucket and followed the steps on screen. Once the bucket was created I clicked on it and in properties I clicked on static web hosting. I saved the settings in this then went to permissions and then CORS configuration. I copied and pasted the CORS configuration from Code Institute and then the same for the bucket policy. I go to ‘Identity and Access Management’ to create a new group. to create a new policy I import s3 and input my arn. Once I have renewed the policy I add it to the group I previously made. I now create a user and download the csv file and put it in a folder for safe keeping on my desktop. I then test the bucket by uploading a random image.

To connect Django to s3 I pip installed django-storages and boto3. I then add storages to installed apps in settings.py. At the bottom of the settings.py file I configure the credentials from AWS and link them to env.py to hide them. I then run the command collectstatic to copy the static files. To test the static files are being loaded I run the app in the server and inspect the network under css, It was successful.

### Add Media To S3

To add media to S3 I create a new file called custo_storages.py and input two classes, one for static files and one for media files that point toward settings.py Then in settings.py I edit the static files location and the static file storage settings. I run the command collectstatic again and run the app to inspect the network and can see that the media is now added to static. I refresh the bucket in AWS and see that the static files are added. I deleted all the files as these have been added into the static directory. Now I edit the media files class and in settings.py I add the media files location and the default file storage.

### Upload all images and products to new postgresql database

Now that the database was set up I could add all the images and products again so they are kept in the postgresql database instead of the django text admin database.

### Travic CI

I am now going to set up Continuous Integration that runs tests on your code every time it is pushed to GitHub.

[![Build Status](https://travis-ci.com/jboyle1/milestone_project_004.svg?branch=master)](https://travis-ci.com/jboyle1/milestone_project_004)


 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
