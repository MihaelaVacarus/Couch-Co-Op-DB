# Couch Co-Op DB Testing Details #

[Main README.md file](https://github.com/MihaelaVacarus/Couch-Co-Op-DB/blob/master/README.md)

View the live project [here](https://couch-co-op-db.herokuapp.com/).

### **Contents** ###

- [Automated Testing](#automated-testing)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [W3C CSS Validation Service](#w3c-css-validation-service)
    - [PEP8 online](#pep8-online)
    - [JSHint](#jshint)
    - [Chrome DevTools Lighthouse](#chrome-devtools-lighthouse)
    - [Responsive Viewer](#responsive-viewer)
    - [Mobile Friendly Test Google Search Console](#mobile-friendly-test-google-search-console)
    - [WEB accessibility by Level Access](#web-accessibility-by-level-access)

- [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Testing Functionalities](#testing-functionalities)
        - [Devices Used for Testing](#devices-used-for-testing)
        - [Further Manual Testing](#further-manual-testing)

- [Bugs](#bugs)

## Automated Testing ##

### [W3C Markup Validator](https://validator.w3.org/)
- No errors found. Validator throws a few warnings about some sections lacking headings, but those can be safely ignored.

### [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- No errors found. Validator throws three warnings which can be safely ignored. 

### [PEP8 online](http://pep8online.com/)
- No errors found. 

### [JSHint](https://jshint.com/)
- No errors found.

### [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
- For Mobile the scores are: 
    - Performance: 80
    - Accessibility: 91
    - Best Practices: 87
    - SEO: 85
I managed to improve performance the score by reducing the size of the images and also by converting the gif loader from gif to webp format. Re the other suggestions from Lighthouse I couldn't figure out straight ways to try them.

- For Desktop the scores are:
    - Performance: 99
    - Accessibility: 94
    - Best Practices: 87
    - SEO: 82

### [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
- I ran the extension on each page of the website and responsiveness checks OK. 

### [Mobile Friendly Test Google Search Console](https://search.google.com/test/mobile-friendly)
- The result is that the page is mobile friendly.

### [WEB accessibility by Level Access](https://www.webaccessibility.com/)
- The compliance result score is 92%.

[Back to contents](#contents)

## Manual Testing ##

### Testing User Stories
- This part of the testing can be found in a separate document [here](./testing-user-stories.pdf)

### Testing Functionalities
| Home page|    Yes/No     |  
| ------------- |:-------------:|
| Logo redirects to Home.| Y |
| Navigation displays different options if a user is signed in vs is signed out.| Y |
| Navigation collapses to a hamburger menu on smaller devices and remains fixed to the top. | Y |
| All navigation links redirect to their corresponding pages. | Y |
| Parallax slides as intended. | Y |
| Links in intro redirect to the corresponding pages. | Y |
| Footer social media and legal content links redirect to their corresponding sites. | Y |
| Footer sections are fully responsive on smaller devices. | Y |
| Loader works as intended while browsing pages that take longer to load. | Y |
---
| Games page|    Yes/No     |  
| ------------- |:-------------:|
| Search bar searches by name, genre and platform. | Y |
| Clear button resets the search and display all games newly..| Y |
| Hover effects on game cards work as intended.| Y | 
| Game cards are displayed at an appropriate size and responsiveness works as expected.| Y | 
| Link on game cards redirect to the corresponding game page.| Y | 
| If search is has zero hits, flash message displays informing of the search results.| Y | 
---
| Game page|    Yes/No     |  
| ------------- |:-------------:|
| Page is responsive and all intended information is displayed.| Y |
| For guests and registered visitors (RV), shopping link displays and works as intended.|Y|
| For RV, favourite button displays and adds game as favourite.| Y | 
| If a user already marked a game as favourite, this cannot be added again and a flash message informs of this.| Y | 
| If a user marks a game as a favourite, a flash message informs the user that the game has been added successfuly.| Y | 
| Edit and delete buttons only display for RV that added that same game previously, as intended. | Y |
| Delete button prompts a modal asking for confirmation. Clicking Yes deletes the game, while clicking Cancel cancels the action of deletion. | Y | 
| Comment input field can only post comments from RV and it's only visible to them.| Y |
| Comment input field validates correctly according to min characters length and posts on the dashboard below.| Y |
| Users cannot post empty comments.|Y| 
| Dashboard with all comments belonging to each game display as intended. | Y |
| If a guest tries to edit the URL to post a comment without being registered, a flash message will display informing the guest would need to sign in first and redirects to the sign in page.|Y|
| Dashboard with all comments belonging to each game display as intended. | Y |
---
| Edit game page|    Yes/No     |  
| ------------- |:-------------:|
| If a guest tries to edit the URL to edit a game, a flash message will display informing the guest would need to sign in first and redirects to the sign in page.| Y |
| All fields validate correctly as intended.|Y|
| Cancel button works as expected and redirects user to the general games page.| Y | 
| The Update Game button works as expected and updates game details, then flashes a confirmation message to the user.| Y | 
---
| My Account page|    Yes/No     |  
| ------------- |:-------------:|
| If a guest tries to edit the URL to access My Acccount, a flash message will display informing the guest would need to sign in first and redirects to the sign in page.|Y|
| Games marked as favourite by the user in session display correctly and can be accessed by clicking on them.| Y |
| Comments posted by the user in session display as intended and show to which games they belong.| Y |
---
| Add Game page|    Yes/No     |  
| ------------- |:-------------:|
| If a guest tries to edit the URL to access Add Game, a flash message will display informing the guest would need to sign in first and redirects to the sign in page.| Y | 
| All fields validate correctly as intended.| Y | 
| Submit Game button works as intended and add the new game to the db.|Y| 
| When a game is submitted, a flash message informs the user that the game has been added successfuly and redirects to the Games page.| Y | 
---
| Sign Out page|    Yes/No     |  
| ------------- |:-------------:|
| Sign Out functionality removes the user from session cookies and closes the session.| Y |
---
| Sign In page|    Yes/No     |  
| ------------- |:-------------:|
| Input fields validate as intended.| Y |
| If username or password are incorrect, a flash message will inform the user.| Y |
| Sign In button signs in the user correctly.| Y |
---
| Sign Up page|    Yes/No     |  
| ------------- |:-------------:|
| Input fields validate as intended.| Y |
| If username already exists, a flash message informs the user and clears the form.| Y |
| Once a valid username and password are entered, the account is created by clicking the Sign Up.| Y |
--- 
| Website terms of use page|    Yes/No     |  
| ------------- |:-------------:|
| Page is responsive on all device sizes.| Y |
| Links within the text redirect to other pages as intended.| Y |
| Clicking on the email will prompt the user to write an email.| Y |
| Scrollspy works as intended to navigate the several sections.| Y |
--- 
| Website privacy policy|    Yes/No     |  
| ------------- |:-------------:|
| Page is responsive on all device sizes.| Y |
| Links within the text redirect to other pages as intended.| Y |
| Clicking on the email will prompt the user to write an email.| Y |
| Scrollspy works as intended to navigate the several sections.| Y |
---
| Error handler for 404 errors|    Yes/No     |  
| ------------- |:-------------:|
| 404 error template displays when trying to access unfound pages.| Y |
| 404 error template provides a link to redirect RV and guests back to Games.| Y |

- I couldn't reproduce the environment to test errors 500 and 503, but these have been created the same way as 404 error template, and that route tested ok, so I safely assume the other two would as well.
- CRUD functionality works as expected for Admin user, that is, with all the enabled rights.

#### Devices Used for Testing
- Tested on Macbook Pro and Iphone 12.

#### Further Manual Testing
- Tested by several friends and family. 
- Code and website reviewed by Code Institute Slack community.

[Back to contents](#contents)

## Bugs ##
---
| Bug Description| Comments | Resolved (Yes/No) |  
| ------------- |:-------------:| :-------------:|
| On the edit game functionality, even if a user doesn't make any changes to the game details, and then clicks **Update Game**, a flash message would still display reading "Game Successfully Updated".| I discussed this with my mentor and he said it's not a real bug and can be left as it is.| Y |
| If a user in session edits the URL to http://couch-co-op-db.herokuapp.com/sign_out, the user will be signed out without even clicking the Sign Out button.| I discussed this with my mentor and he said it's not a real bug and can be left as it is.| Y |
| If the URL in the Account page is changed to another username, the flash message would display the changed name, although the profile would still be the one belonging to the user in session. | e.g. http://couch-co-op-db.herokuapp.com/account/admin changed to http://couch-co-op-db.herokuapp.com/account/mihaela would show admin's account but the headline would read "Mihaela's Account". | Y |
| Validation for commenting input field allows comments made up of just spaces to be posted.| This was fixed by using the strip Python method. | Y |
| When adding a new game to the DB, for the image URL field, there is not validation to check if indeed it is a URL.| I am looking into implementing regex to fix this. For now, I just changed the input field type to URL to at least have some basic default validation. | N |
| The same game can be added several times to the DB.| I discussed this with my mentor and as much I could implement some defensive programming, there are many ways to go around it. For example, users could submit a game named differently just by a character and that produce the same result. Unfortunately, there is not a unique feature to identify each game and determine based on that if it already exists or not. | N |
| If the URL for editing a game is modified by a user in session to modify a game not added by that same user, the URL still redirects to the edit game page. However, the changes do not save.| This does not seem to be a bug, as it would not save any changes, but it is something I would like to look into, once I have more knowledge of Python routes. |N|

[Back to contents](#contents)