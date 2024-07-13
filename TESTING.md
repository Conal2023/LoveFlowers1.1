# LoveFlowers.ie - Testing

## Validation 


### HTML

The HTML was inspected by accessing the page source and copying the code into the [W3C Validator](https://validator.w3.org/). It returned no errors or warnings, indicating that the HTML code is valid. This was done for all pages. 

![HTML](media/readme/html_validator.jpg)


### CSS

The CSS for all CSS files was validated using [Jigsaw Validator](https://jigsaw.w3.org/css-validator/).

![CSS](media/readme/css_validator.jpg)


### Manual Testing


`Nav Bar`

|   Feature  |                                               Expected Outcome                                             |                  Test Performed                 |                           Result                          | Test Outcome |
|:----------------:|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------:|:----------------------------------------------------------------:|:------------------:|
|       Logo       |                                                 Goes to Home page                                                 |                   Click on the Logo                   |                   Brings the user to Home Page                   |        Pass        |
|   All Products   |   Drop down appears to filter by, once filter is clicked brings you to all products filtered by filter selected   |        Click on All Products and select filter        |   Brings user to All Products Page filtered to selected filter   |        Pass        |
| Seasonal Flowers | Drop down appears to filter by, once filter is clicked brings you to Seasonal Flowers filtered by filter selected |      Click on Seasonal Flowers and select filter      | Brings user to Seasonal Flowers Page filtered to selected filter |        Pass        |
|       Gifts      |       Drop down appears to filter by, once filter is clicked brings you to Gifts filtered by filter selected      |            Click on Gifts and select filter           |       Brings user to Gifts Page filtered to selected filter      |        Pass        |
|     Funerals     |     Drop down appears to filter by, once filter is clicked brings you to Funerals filtered by filter selected     |          Click on Funerals and select filter          |     Brings user to Funerals Page filtered to selected filter     |        Pass        |
| Customer Support |                                Drop down appears for user the select a page to vist                               | Click on Customer Support and select a page from list |                   Brings user to page selected                   |        Pass        |
|     Facebook     |                                               Goes to Facebook Page                                               |                 Click on Facebook Logo                |                   Brings user to Facebook Page                   |        Pass        |
|    My Account    |                                Drop down appears for user to select a page to vist                                |    Click on My Account and select a page from list    |                   Brings User to page selected                   |        Pass        |
|        Bag       |                                                Goes to Shopping Bag                                               |                       Click Bag                       |                 Brings user to Shopping Bag Page                 |        Pass        |


`Footer`

|         Features         | Expected Outcomes |             Test Performed            |              Result              | Test Outcome |
|:------------------------:|:-----------------:|:-------------------------------------:|:--------------------------------:|:------------:|
| Stay In Touch (Facebook) |  Goes to Facebook | Clicked on Follow us on Facebook link | Brings the user to Facebook Page |     Pass     |
|         MailChimp        |     Subscribes    |          Enter Email Address          | User is subscribed to newsletter |     Pass     |


`Contact Us`

|     Feature     |                      Expected Outcome                     |        Test Performed        |            Result           | Test Outcome |
|:---------------:|:---------------------------------------------------------:|:----------------------------:|:---------------------------:|:------------:|
| Contact Us Link |                Goes to the Contact Us Page                |  Clicked on the Contact Us   | Goes to the Contact Us Page |     Pass     |
|  Submit Button  | Submits the contact us request & goes to the Success Page | Clicked on the Submit Button |   Goes to the Success Page  |     Pass     |


`FAQ Page`

| Features | Expected Outcomes |          Test Performed          |            Result           | Test Outcome |
|:--------:|:-----------------:|:--------------------------------:|:---------------------------:|:------------:|
| FAQ Link |  Goes to FAQ Page | Clicked on Follow us on FAQ link | Brings the user to FAQ Page |     Pass     |


`Testimonial Page`

|     Features     |     Expected Outcomes    |              Test Performed              |                Result               | Test Outcome |
|:----------------:|:------------------------:|:----------------------------------------:|:-----------------------------------:|:------------:|
| Testimonial Link | Goes to Testimonial Page | Clicked on Follow us on Testimonial link | Brings the user to Testimonial Page |     Pass     |


`Register`

|    Feature    |                 Expected Outcome                 |        Test Performed        |           Result          | Test Outcome |
|:-------------:|:------------------------------------------------:|:----------------------------:|:-------------------------:|:------------:|
| Register Link |             Goes to the Register Page            |   Clicked on the Register    | Goes to the Register Page |     Pass     |
| Submit Button | Submits the registration & goes to the Home Page | Clicked on the Submit Button |   Registers the user and goes to the Home Page   |     Pass     |


`Login`

|    Feature    |              Expected Outcome             |        Test Performed        |               Result              | Test Outcome |
|:-------------:|:-----------------------------------------:|:----------------------------:|:---------------------------------:|:------------:|
|   Login Link  |           Goes to the Login Page          |       Clicked on Login       |       Goes to the Login Page      |     Pass     |
|    Sign Up    |         Goes to the Register Page         |      Clicked on Sign up      |     Goes to the Register Page     |     Pass     |
| Submit Button | Submits the login & goes to the Home Page | Clicked on the Submit Button | Logs in and goes to the Home Page |     Pass     |


`Logout`

|     Feature     |     Expected Outcome    |         Test Performed        |                      Result                      | Test Outcome |
|:---------------:|:-----------------------:|:-----------------------------:|:------------------------------------------------:|:------------:|
|   Logout Link   | Goes to the Logout Page |       Clicked on Logout       |              Goes to the Logout Page             |     Pass     |
| Sign Out Button |    Logs the user out    | Clicked on the Log Out Button | Logs the user out and goes back to the Home Page |     Pass     |



## Bugs

 - Currently having an issue with the project since switching from Gitpod to Gitpod Enterprise. Tutor support have advised that this is because my project is using a newer version of Python then what Gitpod Enterprise is using. They have advised me that I would need to run the command "pyenv install 3.9.19 && pyenv global 3.9.19" everytime I start up my project. They advised me there is no permanent fix to this issue. 

### Fixed Bugs

 - I originally had a issue with webhooks where after a purchase went through the email confirmation wouldnt come through on the terminal. After trying to figure out the issue I had to contact Tutor support who advised me that I hadnt set up the Hosted Endpoints correctly. Once fixed the emails were sent to the terminal correctly.

## Wave Aim Accessibilty Checker

 - Initially, there were several contrasting issues identified during the initial testing phase. However, all of these issues were successfully addressed and resolved. Currently, there are no contrasting issues detected on the website, indicating that it is now functioning smoothly without any noticeable problems.

 - On the product pages, there are alerts on the prices, indicating that these are possible headings. However, since these are not actually headings but rather fields for inputting information, I agreed that they don't need to be changed.

 ![Alerts_Prices](media/readme/alerts_prices.jpg)

 - On the profile page I am getting errors to advise of missing form labels. After spending a lot of time on trying to fix this, nothing I did worked and I eventually gave up. 

 ![Alerts_Profile](media/readme/alerts_profile.jpg)


## Lighthouse

I employed Chrome Developer Tool Lighthouse to test the Performance, Accessibility, Adherence to best practices and SEO. 

### Home Page:

![Home Page](media/readme/homepage_lighthouse.jpg)

### Contact Page:

![Contact Page](media/readme/contactpage_lighthouse.jpg)

### FAQ Page:

![FAQ Page](media/readme/faq_lighthouse.jpg)

### Testimonial Page:

![Testimonial Page](media/readme/testimonial_lighthouse.jpg)

### Products Page:

![Products Page](media/readme/products_lighthouse.jpg)

### Shopping Bag:

![Shopping Bag](media/readme/bag_lighthouse.jpg)

### Sign In Page:

![Sign In Page](media/readme/signin_lighthouse.jpg)

### Sign Out Page:

![Sign Out Page](media/readme/signout_lighthouse.jpg)

### Sign Up Page:

![Sign Up Page](media/readme/signup_lighthouse.jpg)

