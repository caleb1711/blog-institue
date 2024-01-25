# Blogs Institute
Blogs Institute is a full-featured blogging platform that empowers users to share their thoughts, ideas, and stories with the world. Whether you're an aspiring writer or a seasoned blogger, our platform provides the tools and features you need to create, manage, and engage with your blog content.


## Table of Contents

1. [Introduction](#introduction)
2. [Screenshots](#screenshots)
3. [Features](#key-features)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Setup Virtual Environment](#setup-virtual-environment)
5. [Code Structure](#code-structure)
6. [Continuous Integration and Testing](#continuous-integration-and-testing)
7. [Deployment](#deployment)
8. [Acknowledgments](#acknowledgments)
9. [Contact](#contact)


## Introduction

Blogs Institute offers a unique platform for bloggers, providing a user-friendly interface and robust features. This README aims to guide users through the setup, features, and deployment of the platform.


- __Home Page__

  - User can see all of the blogs in home page after clicking on read more button user will go to the blog detail page .
  - User can leave a comment on blog in blog details page so comment will be saved in database. 


![1](https://github.com/caleb1711/blog-institue/assets/130179631/4ba8171d-2886-4b93-9c23-892850f169dd)
![2](https://github.com/caleb1711/blog-institue/assets/130179631/5a01b7d1-1a5c-4176-a8d5-071eae601b30)



- __Signup Page__

  - User Can register on our website and then create the blogs and all CRUD will be perform .
  - User will enter first name , last name,  email, phone_number and password for registration.
  - user can not use same email for other account creation.
 
    ![3](https://github.com/caleb1711/blog-institue/assets/130179631/283c3cef-035a-4a1f-b754-2d868547029c)


    
- __Login Page__
   - After registration user will be able to login to the system .
   - User will be able to acces all the features in our site .
 
     ![4](https://github.com/caleb1711/blog-institue/assets/130179631/28e7ce4d-7391-4830-8b3b-8f5f8a9485c5)




- __Forgot Password__
   - User if user forgot his password so he will be able to reset the password.
   - User enter his email and system generate a link for reset password and send a email to user .
   - System will send the email to user
 
     ![5](https://github.com/caleb1711/blog-institue/assets/130179631/3dc65236-26c0-49bc-827b-c21895d4de88)



- __Reset Password__
   - User click on reset link and he will go to the reset password page.
   - User can easily change his password and easily recover the passowrd.
 
     ![6](https://github.com/caleb1711/blog-institue/assets/130179631/a0debbd0-b24f-4264-8c4b-0ca4e8a9acb8)




- __My Blogs Page__
   - After login user can access the my blogs page .
   - user can see all of his blogs.
   - User can edit a blog and also delete the blog.
 
     ![7](https://github.com/caleb1711/blog-institue/assets/130179631/d3dd2699-f990-4139-a3e6-b852dcf927d2)



- __Edit Blog Page__
   - User can edit his blog easily user will click on edit button and he will go to the edit page .
   - edit page will show prefilled data about blog.
 
     ![8](https://github.com/caleb1711/blog-institue/assets/130179631/23dd4a2c-de50-4b04-b65d-afb52291e2e3)




- __Add Blog Page__
   - User can add the blog  easily .
 
     ![9](https://github.com/caleb1711/blog-institue/assets/130179631/cad14b0c-275e-49d6-8cca-c23fbe53f193)


     
- __Admin Side__
   - Admin User will be able to do anything on site. 
   - Admin user can create the other admin users.
 
     ![10](https://github.com/caleb1711/blog-institue/assets/130179631/e6468215-f4cc-489c-ba10-0ab7cf282539)



- __LOGOUT__
   - User can logout to the system.

- __HEADER__
   - The header of our blogging platform, Blogs Institute, provides users with easy navigation and essential information.
   - Logo: Our distinctive logo is prominently displayed, representing the Blogs Institute brand. Click on it to return to the homepage from anywhere on the site.
   - Navigation Menu: The navigation menu is organized for easy access to different sections of the platform. It includes links to the homepage, user profile, blog management, and the login/logout option. For mobile users, the menu is collapsible for a smooth browsing experience.
   - User Account: Once you've signed in, your profile picture or avatar is displayed in the header, along with options for account settings and log out.

- __FOOTER__
   - Copyright Information: We respect intellectual property rights. The footer contains copyright information to protect user-generated content and ensure proper attribution.

 - __ScreenShots__


   ![11](https://github.com/caleb1711/blog-institue/assets/130179631/e8f441c7-20e6-4334-975a-68c1a8f3f2f1)

   - Mobile View
   ![12](https://github.com/caleb1711/blog-institue/assets/130179631/2f38b058-0d26-4a10-b1d4-fc95cf9d1371)


   ![13](https://github.com/caleb1711/blog-institue/assets/130179631/bb63c72f-84bf-4ddb-9aec-9660747b2a9a)


   ![14](https://github.com/caleb1711/blog-institue/assets/130179631/eec45402-2ed0-465f-8437-89d23216d5c1)


   ![15](https://github.com/caleb1711/blog-institue/assets/130179631/09dd7859-8242-4133-a343-9201ea3389af)


   ![16](https://github.com/caleb1711/blog-institue/assets/130179631/ff3111b6-f775-4859-a259-50cf2e03c00b)


   ![17](https://github.com/caleb1711/blog-institue/assets/130179631/19376861-8d18-4e93-8ba5-79e3cd33910d)


   ![18](https://github.com/caleb1711/blog-institue/assets/130179631/00a104e9-c6a8-4e6c-854e-7add189c951d)


   ![19](https://github.com/caleb1711/blog-institue/assets/130179631/8caac612-6909-4b05-8645-34289fc87e35)



## Key Features

- Full Authentication System
- User account management (create, login, forgot password, reset password)
- Blog post creation with title, content, and images
- Blog post editing and updating
- Blog post deletion
- Commenting on blog posts
- Image upload and display in blog posts and comments


 
- __FONT SIZE__
   - Robot font is used in our website.
 
   - @import url("https://fonts.googleapis.com/css2?family=Poppins&family=Roboto:wght@500&display=swap");
   - @import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");
   - @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap");



- __UNFIX BUGS__
   - At Blogs Institute, we are committed to providing a seamless and bug-free experience for our users. We take quality assurance seriously and have conducted thorough manual testing of our website. We are pleased to report that, as of the latest testing, no bugs have been identified.
   - Our testing process involves:
   - Navigating the website on different browsers, including Chrome, Firefox, and Safari, to ensure cross-browser compatibility.
   - Testing the website's functionality on both desktop and mobile devices to ensure responsive design.
   - Exploring all user features, including registration, login, blog creation, editing, commenting, and account management.




  ### Tools
- Front end
- HTML
- CSS
- BOOTSTRAP
- JAVASCRIPT

- Back end
- python
- django
- django templating
- relational database sqllite

  
  


## Getting Started

### Prerequisites

Ensure you have the following dependencies installed:

- asgiref==3.7.2
- Django==4.2.7
- Pillow==10.1.0
- sqlparse==0.4.4
- typing_extensions==4.8.0

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/caleb1711/blog-institute


### Setup virtual environment
Create a virtual environment using python3
```bash
    cd blog-institute
    python3 -m venv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

3. Installation steps:
```bash
    python manage.py migrate
    python manage.py runserver
```

## Code Structure

The codebase is organized into several main components for clarity and maintainability. Here's an overview of the key directories:

- **`/accounts`**: Contains the main Django application logic for the user Profile data.
- **`/blogs`**: Contains the main Django application logic for the blogging platform.
- **`/core`**: The root directory of the project.
- **`/static`**: Stores static files such as CSS, JavaScript, and images.
- **`/templates`**: Holds HTML templates used by the Django templating engine.
- **`manage.py`**: Django's command-line utility for managing the project.
- **`requirements.txt`**: Lists all Python dependencies for the project.

Feel free to explore each directory to understand the specific functionality and organization of the codebase.


## Continuous Integration and Testing

- The project follows best practices for continuous integration and testing to ensure code quality and reliability. Key points in this process include:

### Automated Testing

We have implemented a comprehensive suite of automated tests to validate the functionality of different components. These tests cover unit tests, integration tests, and end-to-end tests. To run the tests locally, use the following command:

```bash

Python3 manage.py test

```



- __VALIDATOR TESTING__
   - VALIDATOR TESTING with wc3 of all the front end .
   - Python testing done is manually
   - Django testing done manually
   - All the features of our Project is Done
    ![20](https://github.com/caleb1711/blog-institue/assets/130179631/809e85c1-8680-4e6f-b556-a491eda53e06)



## DEPLOYMENT

- This site will be deployed on Heroku. Detailed deployment instructions will be provided soon.


## Acknowledgments

We would like to extend our appreciation to the following individuals and resources that have contributed to the development and success of Blogs Institute:

- **Bootstrap and Roboto Fonts**: Special thanks to the Bootstrap framework and Roboto font family for enhancing the visual design and responsiveness of our website.

- **Django**: A big shoutout to the Django framework for powering the backend of our blogging platform.

- **GitHub**: Our project is hosted on GitHub, providing a collaborative and version-controlled environment.


These contributions have played a crucial role in shaping Blogs Institute, and we want to express our sincere thanks to everyone involved.


## Authors

- Calkra15@outlook.com

## Contact

If you have any questions or need support, you can reach me at Calkra15@outlook.com
.
