# Couch Co-Op DB

Couch Co-Op DB is a website for people that enjoy playing couch co-op videogames. The idea for this project is to create a space where players can become registered users and add their favourite games, share tips and tricks and rate them. Site visitors can read about the games and purchase them via a hyperlink to Steam that will provide them with a 20% discount voucher.

---

### **Contents** ###

- [UX](#ux-user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
    - [Design](#design)
        - [Wireframes](#wireframes)
        - [Database](#database)
        - [Fonts](#fonts)
        - [Colors](#colors)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## UX (User Experience) ##

### **Project Goals** ###

The **goal** of this project is to build a website that allows people passionate about videogames to find the most played couch co-op games added by registered users, read comments from the community and get a direct link to purchase the games with a discount voucher.

### **User Stories** ###
#### **New Site Visitor** ####
- As a user, I want to be able to easily navigate to the different site pages.
- As a user, I want to see a page containing all games.
- As a user, I want to be able to register on the site.
- As a user, I want to be able to add new games and add comments.
- As a user, I want to be able to read other member’s reviews.
- As a user, I want to be able to search the site by games names, number of players and platform.
- As a user, I want to be able to find direct links to purchase the games I like.

#### **Returning Site Visitor** ####
- As a user, I want to see my user account profile page.
- As a user, I want to be able to update and/or delete any of the games I have added.
- As a user, I want to be able to mark games as favorites, so I can easily see them from my account page. 
- As a user, I want to be able to leave comments on the other games.

#### **Site Administrator** ####
- As an **Administrator**, I want to be able to add, edit and delete the games details.

### **Site Owner Goals** ###
- Create a co-op gaming community to increase site owner's following on Twitch and rest of social media. 
- Earn money every time a user purchases a game via the link provided on my site.
 

### **Design** ###

#### **Wireframes** ####
The wireframes for the website have been created with [Figma](https://www.figma.com/) and are available [here](https://www.figma.com/file/Z4haTyThhzKwdy75zFupo5/Couch-Co-Op-DB?node-id=0%3A1).
Tablet and mobile devices share the same layout, while a separate design has been created for the desktop views. 

#### **Database** ####

#### - users collection
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectId()
Username|username|String
Password|password|String
Admin|is_admin|String

#### - games collection
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Game ID|_id|ObjectId()
Name|name|String
Description|description|String
Image|image_url|String
Players|number_players|Integer
Release Year|year_release|Integer
Genre|genre|String
Developer|developer|String
Publisher|publisher|String
Platforms|platforms|String
Shop|shop_link|String

#### - favourites collection
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Game ID|_id|ObjectId()
User ID|_id|ObjectId()

#### - comments collection
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Game ID|_id|ObjectId()
User ID|_id|ObjectId()
Date|date_submitted|Timestamp
Comment|comment|String

#### Data Types ####

- ObjectId
- String
- Int32
- Date

#### **Fonts** ####
Roboto Google font with a Sans Serif fallback has been chosen for the entire website.

#### **Colors** ####
The color scheme is based on the colours of the *Moving Out* videogame and generated through the [Coolors](https://coolors.co/) website.
To keep it simple and relatable to the videogames, a two colors palette has been used, see [here](https://coolors.co/f7ba2e-db3549).

[Back to contents](#contents)

---

## Features
 
### Existing Features
The **features** on the website will:
- Allow site visitor to register a user account and access more functionalities, such as: add, comment and mark games as favourite.
- Display all couch co-op games that the community has added to enable visitors to read all the details and comments sharing tips and tricks.
- Provide a direct shopping link for each game to the Steam store, where they can get a 20% discount voucher when purchasing it.

I achieve this by:

- Providing registration and user authentication for users to create an account and see their account details.
- Enabling users to add new games and edit their entries. 
- Linking the game store to each game directly on the website.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Create a dashboard to provide site visitors with statistics about all the games.
- Implement a star rating functionality that allows the users to upvote and downvote games depending on their preferences.

[Back to contents](#contents)

---

## Technologies Used


[Back to contents](#contents)

---

## Testing

[Back to contents](#contents)

---

## Deployment

[Back to contents](#contents)

---

## Credits

### Content

### Media

### Acknowledgements

[Back to contents](#contents)

---
