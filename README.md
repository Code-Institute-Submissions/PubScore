<a href="https://ibb.co/P4MKJ8q"><img src="https://i.ibb.co/Npr5fzc/different-devices.jpg" alt="different-devices" border="0"></a>
# PubScore
[This website](https://pubscore.herokuapp.com/) was created to keep track of the teamscores in a Pubquiz competition.<br>
As competing team you can see how your team is doing in the competition.<br>
As Admin you can add teams to the competiton and update there scores after each pubquiz.<br>
## UX
* User stories
    * Competing Team Goals
        1. As a competing team, I want to be able to see how our team is doing in the ranking.
        2. As a competing team, I want to be able to see if the scores have been updates after the last pubquiz.
        3. As a competing team, I want to be able to leave the competition.
    * Administrator Goals
        1. As the admin, I want to be able to add teams to the competition.
        2. As the admin, I want to be able to update the score for each team.
        3. As the admin, I want to be able to see for which team I have updated the scores to prevent mistakes.
        4. As the admin, I want to be able to substract points in case a mistake does happen.
        5. As the admin, I want to be able to delete a team from the competition in case a team requests this.
        6. As the admin, I want to get a warning before a team is deleted.
        7. As the admin, I want to be able to contact the owner of the site in case of any problems.
        8. As the admin, I don't want other people to be able to use pages from where changes to the database can be made.
* Design
    * Color Scheme
        * Because it is a site for a pubquiz competition, I've used typical beer colors.
    * Typography
        * For the PubScore logo I used the font "Do Hyeon" because it reminds me of a typical Highscore look.
        For the rest of the website I've used the font "Titillium Web" because I think it fits well with "Do Hyeon" and it's easy to read.
    * Imagery
        * The images on this page would come from the competing teams through a url link.
        In case there is no team image, I've created a default images that fits well with the rest of the website.
* Wireframes
    * [Phone Wireframes](https://i.ibb.co/rf2FVSq/mock-up-phone.jpg)
    * [Tablet Wireframes](https://i.ibb.co/L6JzHZW/mock-up-tablet.jpg)
    * [Screen Wireframes](https://i.ibb.co/DGRCB04/mock-up-laptop.jpg)
## Features
* I've made sure the site is responsive and easy to use on different devices.
* The site contains interactive elements like color changes when hovering over elements and a hamburger menu that changes when clicked on.
* The site contains a login option.
* The site contains a logout option.
* The site contains a contact form for the admin in case of problems.
## Technologies used
I have used the following technologys for this project:
* HTML5, because it is the standard markup language for Web Pages
* CSS3, to style the website
* Javascript, for the use of a contact form
* [Python](https://www.python.org), for the backend
* [MongoDB](https://www.mongodb.com), for my database
* BSON, to store my data
* Unittest, for testing my Python code
* [Heroku](https://heroku.com), to deploy my app
* [Gitpod](https://gitpod.io), for my development environment
* [Github](https://github.com), for version control
* [Bootstrap](https://getbootstrap.com/), to make my website responsive and mobile-first
* [Google Fonts](https://fonts.google.com/), to choose and combine my fonts
* [Coolors](https://coolors.co/), to choose my and combine my colors
* [EmailJS](https://www.emailjs.com/), to let the user be able to contact me
## Testing
To make sure there where nog syntax errors, I've used the following validators on my pages:
* [HTML validator](https://validator.w3.org/#validate_by_input)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
### Testing User Stories from User Experience (UX) Section
* Competing Team Goals
    1. As a competing team, I want to be able to see how our team is doing in the ranking.
        * By using the navigation menu I can visit the oveview page to see the rankings
        * On the overview page I can see the current score for my team
    2. As a competing team, I want to be able to see if the scores have been updates after the last pubquiz.
        * On the overview page I can take a look at the last update database
        * If this date is later then the last pubquiz, then I know that the scores have been updated by the admin.
    3. As a competing team, I want to be able to leave the competition.
        * If I contact the admin for this competition, the admin can delete my team from the competition.
* Administrator Goals
    1. As the admin, I want to be able to add teams to the competition.
        * When I'm logged in I get redirected to the admin page witch gives me more information on the possibilities I have as an admin.
        * I can use the menu to go to the add team page.
        * On this page I can fill in a team name, a starting score and a url for a team photo.
        * The site will tell me that a team name and starting score are manditory and a url for a team photo is optional.
        * I can send the new team to the database by clicking the Add team! buton
    2. As the admin, I want to be able to update the score for each team.
        * When I'm logged in I get redirected to the admin page witch gives me more information on the possibilities I have as an admin.
        * I can use the menu to go to the update teams page.
        * On this page I can fill in the points each team has scores in the last pubquiz.
        * I can send the points to the database by clicking the Update score! button.
    3. As the admin, I want to be able to see for which team I have updated the scores to prevent mistakes.
        * When adding points for a team the last update date will change.
        * If it shows me todays date, then I know I have send in the points allready.
        * If it shows me an older date, then I know I still have to add the points.
    4. As the admin, I want to be able to substract points in case a mistake does happen.
        * In case I've added to much points, I can fill in how many points I need to substract.
        * By using the - before the amount of points the score will decrease.
        * I can substract the points by clicking the Update score! button.
    5. As the admin, I want to be able to delete a team from the competition in case a team requests this.
        * When I'm logged in I get redirected to the admin page witch gives me more information on the possibilities I have as an admin.
        * I can use the menu to go to the update teams page.
        * I can click on the Delete team! button for the team that I want to remove from the competition.
        6. As the admin, I want to get a warning before a team is deleted.
        * To prevent mistakes there will be a pop up to ask me if I'm sure I want to delete the team.
        * I can click yes if I'm sure I want to delete the team from the database.
        * If I'm not sure, I can can click no or I can click on the screen outside the pop up.
    7. As the admin, I want to be able to contact the owner of the site in case of any problems.
        * When I'm logged in I get redirected to the admin page witch gives me more information on the possibilities I have as an admin.
        * I can use the menu to go to the contact page.
        * On the contact page I can fill in my name e-mailadress and message.
        * The contact form will let me know all fields are manditory.
        * I can send in the form by clicking the Submit button.
        * A pop up will let me know if my message has been send succesfully or not.
        * By clicking the ok button the form will be cleared automatically.
    8. As the admin, I don't want other people to be able to use pages from where changes to the database can be made.
        * By clicking the login button in the menu I will land on the login page.
        * As an admin I can login by using my own username and personal password.
        * The form will let me know both fields are mandetory.
        * If I use the wrong password and/or username, the page will let me know it's incorrect.
        * As an admin I can also login by using the general admin username and password.
        * When logged in I will be redirected to the admin page with more information on the possibilities I have as an admin.
        * There will be new pages available in the menu after loging in.
        * When I'm not logged in and try to visit the admin pages I will get redirected to the login page.
        * When I'm done I can logout by using the logout button in the navigation menu.
### Further testing
* I've tested this Website on Google Chrome, Microsoft Edge and Firefox browsers.
* I've tested this Website on laptop and mobile.
* I've tested different devices using "inspect" in chrome.
* I've asked for peer reviews on Slack.
* I've asked friends and family to look at the website and give feedback.
* I've written as much Unittest as I could in the given time.
* I've used doctest for pointers during manually testing my site.
### Known bugs
* Doctest let me know I should use _one when working if data from one team in my database (fixed).
## Deployment
This project was created using Github.<br>
From there I used Gitpod.io to write my code.<br>
Then I used commits to git followed by pushes to my GitHub repository.<br>
Later on I've deployed this project to Heroku and used automated pushes to make sure my pushes to GitHub were also made to Heroku.<br>
For deployment on Heroku I've used the following steps:
* Using the terminal command pip freeze > requirements.txt I have created a requirements.txt file.
* Using the terminal command echo web: python app.py > Procfile I have created a procfile.
* I've used git add, git commit and git push to push the requirements and procfile to GitHub.
* I've created a new app on the Heroku website by using the "new" button on my dashboard.
* I gavethe app a name of pubscore and set the region to Europe.
* From the Heroku dashboard I've clicked "Deploy" > "Deployment method" and selected GitHub.
* Confirm the linking of the heroku app to the correct GitHub repository.
* In the heroku dashboard I've clicked "Settings" > "Reveal Config Vars".
* I've added the config vars for my IP, PORT, MONGO_URI, SECRET_KEY, SECRED_PASSWORD_ONE and SECRED_PASSWORD_TWO.
* In the heroku dashboard I've clicked "Deploy".
* In the "Manual Deployment" section of this page I've made sure the master branch is selected and I've clicked "Deploy Branch".
* The site was now successfully deployed.
## Credits
### Content
* All the content for this website was writen by the devoloper herself.
### Media
* The no-photo image was created by the developer herself.
* I've used photos from "Dennis Magati", "Matheus Ferrero" and "Nicolas Postiglioni" as team photos to fill my database with some examples.
### Acknowledgement
* I would like to thank my mentor for the feedback througout this project.
* I would like to thank tutor support for helping me where needed.
* I've added comments with links when using code from other people, I would like to thank these people as well for providing helpfull information on the internet.