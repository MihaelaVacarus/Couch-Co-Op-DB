# Couch Co-Op DB Testing Details #

[Main README.md file](https://github.com/MihaelaVacarus/Couch-Co-Op-DB/blob/master/README.md)

View the live project [here](https://couch-co-op-db.herokuapp.com/).

### **Contents** ###

- [Automated Testing](#automated-testing)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [W3C CSS Validation Service](#w3c-css-validation-service)
    - [PEP8 online](#pep8-online)
    - [Chrome DevTools Lighthouse](#chrome-devtools-lighthouse)
    - [Responsive Viewer](#responsive-viewer)
    - [Mobile Friendly Test Google Search Console](#mobile-friendly-test-google-search-console)
    - [WEB accessibility by Level Access](#web-accessibility-by-level-access)

- [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Testing Functionalities](#testing-functionalities)

- [Bugs](#bugs)

## Automated Testing ##

### W3C Markup Validator
- No errors found. Validator throws a few warnings about some sections lacking headings, but those can be safely ignored.

### W3C CSS Validation Service
- No errors found. Validator throws three warnings which can be safely ignored. 

### PEP8 online
- No errors found. 

### Chrome DevTools Lighthouse
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

### Responsive Viewer
- I run the extension on each page of the website and responsiveness checks OK. 

### Mobile Friendly Test Google Search Console
- The result is that the page is mobile friendly.

### WEB accessibility by Level Access
- The compliance result score is 92%.

## Manual Testing ##

### Testing User Stories
- This part of the testing can be found in a separate document [here](/workspace/Couch-Co-Op-DB/static/testing/testing-user-stories.pdf).

### Testing Functionalities
