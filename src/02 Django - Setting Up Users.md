# Set up user accounts and manage access

Create New Test user
Account: test_user01
Password: Frito(13(Skip))

## Learning points
###Login services now defined as a class
- The url lookup in the HTML page uses the url name to resolve the view
- The vie wthen creates the page
- The login page view is systems defines and assumes the location of
the login page to be in a directory called registration
- One the login page is entered into registration you are good.
- The login services used to be defined as a view
- It is now defines as a class and requires code to be cmodofoed to 
correclty call the pages.

## Resources
- [How to set up login with Django 3.2.9](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in)

## Task List

- ✅ Create the users app
- ✅ Add users app to settings
- ✅ include the  URLS from users in root URLs
- ✅ Build login page
  - ✅ Create the Login Page in users app URL
  - ✅ Create the login template 
  - ✅ Add link to login page on the base template
  - ✅ Use the login page
- Create Logout Page
  - Create Logout URL
  - Create logout view
  - add base template link to logout view
- Create registration Page
  - Add Registration URL to users URLS
  - Create register view
  - Create the register template
  - Link to registration page in base teemplate
  - 