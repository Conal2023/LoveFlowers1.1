## Deployment 

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To Obtain your own Postgres Database, sign up with your Github account, then follow these steps:

 - Click Create New Instance to start a new database.

 - Provide a name (Recommonend using the name of your project).

 - Select the Tiny Turtle (Free) plan.

 - You can leave the Tags blank.

 - Select the Region and Data Center closest to you.

 - Once created, click on the new satabase name to view the database URL and password.


### Stripe API 

This project uses [Stripe](https://stripe.com) to handle e-commerce payments. 

Once you've created a Stipe account and logged in, follow these steps to connect your project:

 - From your Stipe dashboard, expand the "Get your test API keys" section.

 - You'll find two keys here:

   - 'STRIPE_PUBLIC_KEY' = Publishable Key (Begins with pk).
   - 'STRIPE_SECRET_KEY' = Secret Key (Begins with sk). 

To include Stripe Webhooks as a backup in case users prematurely close the purchase-order page during payment:

 - From your Stripe dashboard, CLick Developers, then select Webhooks.

 - Click Add Endpoint.

    - Add your deplyed site link.

 - Select receive all events.

 - Click Add Endpoint to complete the process.

 - You will find a new key here:

    - 'STRIPE_WH_SECRET' = Signing Secret (Webhook) key (begins with wh).


### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verifications or for order confirmations. 

Once you have created a Gmail account and have logged in, follow these steps to connect your project:

 - Click on the Account Settings in the top-right corner of Gmail.

 - Click on the Accounts and Import tab.

 - In the "Change account settings" section, click on the link for Other Google Account Settings.

 - From the new page, select Security on the left. 

 - Select 2-Step Verification to turn it on.

 - Once verified, select Turn on for 2FA.

 - Navigate back to the Security page, and you will see a new option called App Passwords.

 - This might prompt you once again to confirm your password and account.

 - Select Mail for the app type.

 - Select Other (Custom Name) for the device type.

   - Enter any custom name, such as 'Django'.

 - You will be provided with a 16-character password (API Key).

   - Save this locally, as you cannot access this key again later!

   - 'EMAIL_HOST_PASS' = user's 16-character API key.

   - 'EMAIL_HOST_USER' = user's own personal Gmail address. 


### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that allows developers to build, run and manage applications entirely in the cloud. 

After setting up your account, follow these deployment steps:

 - In the top-right corner of your Heroku Dashboard, click New and select Create New App from the dropdown menu. 

 - Choose a unique name for your app (Recommond using your project name!), select a region (EU or USA), click Create App.

 - In the new app's Settings, click Reveal Config Vars to set your environment Variables. 

 | Key | Value |
| --- | --- |
| AWS_ACCESS_KEY_ID | user's own value |
| AWS_SECRET_ACCESS_KEY | user's own value |
| DATABASE_URL | user's own value |
| EMAIL_HOST_PASS | user's own value |
| EMAIL_HOST_USER | user's own value |
| SECRET_KEY | user's own value |
| STRIPE_PUBLIC_KEY | user's own value |
| STRIPE_SECRET_KEY | user's own value |
| STRIPE_WH_SECRET | user's own value |

Heroku requires two additional files for depolyment:
 
 - 'requirements.txt'

 - 'Procfile'

Install the projects dependencies with:

 - 'pip3 install -r requirements.txt'

Create the Profile with the following command:

 - 'echo web: gunicorn app_name.wsgi > Profile'

 - Replace app_name with the name of your primary Django app (the one with 'settings.py').

To deply via Heroku, connect your Github repository to the newly created app by either:

 - Selecting Automatic Deplyment from the Heroku app, or 

 - Set the Heroku remote: 'heroku git:remote -a app_name' (replace app_name with your apps name)

 - After performing the standard Git Add, Commit and Push to Github, type:

   - 'git push heroku main'

Your Project should now be connected and deployed to Heroku!


### Local Deployment

You can clone or fork this project to create a local copy on your own system. 

Regardless of the method you choose, you will need to install the necessary packages listed in the requirements.txt file:

 - 'pip3 install -r requirements.txt'


### Cloning 

To clone the repsitory, follow these steps:

 - Visit the [GitHub repository](https://github.com/Conal2023/LoveFlowers1.1)
 - Click the Code button above the list of files.
 - Choose whether to clone using HTTPS, SSH, or GitHub CLI, and click the copy button to copy the URL to your clipboard.
 - Open Git Bash or Terminal.
 - Navigate to the directory where you want the cloned repository.
 - In your IDE Terminal, enter the following command to clone the repository:

   - git clone https://github.com/Conal2023/LoveFlowers1.1

 - Press Enter to create your local clone.


### Forking

Forking a GitHub repository creates a copy of the original repository in your GitHub account, allowing you to view and/or make changes without affecting the original owner's repository. Follow these steps to fork the repository:

 - Log in to Github and go to the [GitHub Repository](https://github.com/Conal2023/LoveFlowers1.1).

 - At the top of the repository (above the "Settings" button on the menu), click the Fork button.

 - After clicking, you will now have a copy of the original repository in your own Github account.