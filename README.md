# The-Hood
This is a neighborhood application which allows users to be connected to his or her neighborhood.


## Description
This web-app allows a user to create a Profile, Join Neighborhood,See Posts and add Businesses alongside see other Businesses,Posts and Neighborhoods.


## Features

As a user of the application you will be able to:

1. A user can log in.
2. A user can sign up.
3. View neighborhoods. 
4. A user can view and add businesses.
5. A user can view posts,health servicess and get authority details.
6. A user is also able to change his or her profile,add bio .


### Installation and setup instructions

1. Clone this repo: git clone https://github.com/asandelarvine/The-Hood
2. The repo comes in a zipped or compressed format. Extract to your preferred location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
4. pip install -r requirements.txt
5. On your terminal,Create database instagram using the command below.

       CREATE DATABASE instagram;
6. Migrate the database using the command below

       python3.8 manage.py migrate
7. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

       python manage.py runserver
8. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

    

### LIVE LINK
Live link : https://hood-2022.herokuapp.com/


## Admin Dashboard

[Admin Dashboard Login]()  with credentials

    username : `MyHood`

    password : `myhoodpassword`

### Known Bugs
Elements re-arrange themselves unequally on different screen sizes.

### Behaviour Driven Development
The program should return all projects on the directories page
Given:All projects
When: Url is changed to directory page
Then: All projects are displayed

Program should show the project with the highest number of votes on the caraousel on the home page
Given:A Project with the highest votes
When: Home page is accessed
Then: Project with highest votes is displayed.

Admin site should be displayed when "admin/" url is chosen
Given: An admin url
When: User enters admin url in browser
Then: Admin Login is displayed

User authentication occurs when Admin tries to Login
Given:Admin page is accessed
When: User tries to login
Then: User details are authenticated to confirm if user is an admin

User session should end when logout url is chosen
Given:Logout option is given
When: User chooses logout option
Then: User session is ended

### Technologies Used
Visual Studio used as  the source code editor.
Git and Github were used as my local and online repositories respectively.
Django was used as the framework 
Heroku was used in deploying the live site


### Support and contact details
Contact me through my email:asandelarvine@gmail.com



