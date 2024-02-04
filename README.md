# Blogs Institute
Blogs Institute is a full-featured blogging platform that empowers users to share their thoughts, ideas, and stories with the world. Whether you're an aspiring writer or a seasoned blogger, our platform provides the tools and features you need to create, manage, and engage with your blog content.

## Intent

The primary intent behind the creation of Blogs Institute is to offer a comprehensive and user-friendly platform for individuals who want to express themselves through blogging. We aim to:

1. Empower Writers: Provide a space where writers of all levels can showcase their creativity, expertise, and unique perspectives.

2. User-Friendly Experience: Ensure a seamless and intuitive experience for both novice and experienced bloggers with a user-friendly interface.

3. Feature-Rich Platform: Offer a plethora of features, including a full authentication syste

## Table of Contents

1. [Introduction](#introduction)
2. [Screenshots](#screenshots)
3. [Features](#key-features)
4. [Security Features](#security-features)
5. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Setup Virtual Environment](#setup-virtual-environment)
6. [Code Structure](#code-structure)
7. [Data Schema and Relationships](#data-schema-and-relationships)
7. [Continuous Integration and Testing](#continuous-integration-and-testing)
8. [Deployment](#deployment)
9. [Acknowledgments](#acknowledgments)
10. [Contact](#contact)


## Introduction

Blogs Institute offers a unique platform for bloggers, providing a user-friendly interface and robust features. This README aims to guide users through the setup, features, and deployment of the platform.


- __Home Page__

  - User can see all of the blogs in home page after clicking on read more button user will go to the blog detail page .
  - User can leave a comment on blog in blog details page so comment will be saved in database. 


![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-2024-02-04-04_54_27](https://github.com/caleb1711/blog-institue/assets/130179631/1a0bf2c6-59db-4c64-ab7c-6722100a2b91)




- __Signup Page__

  - User Can register on our website and then create the blogs and all CRUD will be perform .
  - User will enter first name , last name,  email, phone_number and password for registration.
  - user can not use same email for other account creation.
 
    ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-signup-2024-02-04-04_56_19](https://github.com/caleb1711/blog-institue/assets/130179631/72740f21-a559-48c2-a8b7-d918a6dc131f)



    
- __Login Page__
   - After registration user will be able to login to the system .
   - User will be able to acces all the features in our site .
 
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-login-2024-02-04-04_56_55](https://github.com/caleb1711/blog-institue/assets/130179631/cb45b9c7-aa94-43fd-870a-4e53b6fdb433)




- __Forgot Password__
   - User if user forgot his password so he will be able to reset the password.
   - User enter his email and system generate a link for reset password and send a email to user .
   - System will send the email to user
 
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-forgot-2024-02-04-04_57_44](https://github.com/caleb1711/blog-institue/assets/130179631/3bc80c75-ed02-4168-9305-a643ab64e2bb)




- __Reset Password__
   - User click on reset link and he will go to the reset password page.
   - User can easily change his password and easily recover the passowrd.
 
     ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-reset-6e556103-aced-4f68-a3b7-4a0a7242dc7a-2024-02-04-04_58_42](https://github.com/caleb1711/blog-institue/assets/130179631/1b409099-c619-457d-9559-e7510a02d805)





- __My Blogs Page__
   - After login user can access the my blogs page .
   - user can see all of his blogs.
   - User can edit a blog and also delete the blog.
 
     ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-myblogs-2024-02-04-04_59_56](https://github.com/caleb1711/blog-institue/assets/130179631/35e78c59-ef33-4e7d-9ad6-3a21ee0ca0af)




- __Edit Blog Page__
   - User can edit his blog easily user will click on edit button and he will go to the edit page .
   - edit page will show prefilled data about blog.
 
     ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-editblog-19-2024-02-04-05_00_31](https://github.com/caleb1711/blog-institue/assets/130179631/f4fbc983-8127-48a7-88f1-e8faff52488d)




- __Add Blog Page__
   - User can add the blog  easily .
 
     ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-addblog-2024-02-04-05_01_05](https://github.com/caleb1711/blog-institue/assets/130179631/93ff24df-fa76-4200-a6fb-f070199274f3)


- __About Us Page__
   - About us
     ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-about-2024-02-04-05_34_26](https://github.com/caleb1711/blog-institue/assets/130179631/ee81e343-a04c-4c34-bd07-278032e4837e)


- __Contact Us Page__
   - Contact us
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-contact-2024-02-04-05_36_51](https://github.com/caleb1711/blog-institue/assets/130179631/03250948-d533-4c26-8c6d-719cdfd746e6)


- __Privacy policy Page__
   - Privacy policy
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-privacy-2024-02-04-05_37_19](https://github.com/caleb1711/blog-institue/assets/130179631/2bd8b920-964f-459e-b1bc-db74e0b0376e)

 
- __Term's & conditions Page__
   - Term's & conditions
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-terms-2024-02-04-05_37_58](https://github.com/caleb1711/blog-institue/assets/130179631/d6fb92a4-7024-455f-9a28-3c6cdb98a7dc)


- __Disclaimer Page__
   - Disclaimer
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-disclaimer-2024-02-04-05_38_43](https://github.com/caleb1711/blog-institue/assets/130179631/1f2de293-f92e-4ce0-92b6-d322cc3eb7f7)

  
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


      ![Screenshot from 2024-02-04 05-02-09](https://github.com/caleb1711/blog-institue/assets/130179631/5d10c23e-f907-40fa-a3e7-04b5345db6be)


- __FOOTER__
   - Copyright Information: We respect intellectual property rights. The footer contains copyright information to protect user-generated content and ensure proper attribution.
 
     ![image](https://github.com/caleb1711/blog-institue/assets/130179631/7b5537f5-f626-4a83-8d9b-7d188d84845c)


 - __ScreenShots__


   ![11](https://github.com/caleb1711/blog-institue/assets/130179631/e8f441c7-20e6-4334-975a-68c1a8f3f2f1)

 - __Mobile View__
 - __Home page mobile view__

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-2024-02-04-05_55_10](https://github.com/caleb1711/blog-institue/assets/130179631/75e1f88e-3847-406d-b527-965b38605024)



   - Login page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-login-2024-02-04-05_21_38](https://github.com/caleb1711/blog-institue/assets/130179631/7e1ffc10-96a3-4124-9977-c1af1c95282a)



   - Sign-up mobile view
     
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-signup-2024-02-04-05_22_21](https://github.com/caleb1711/blog-institue/assets/130179631/1326cc0e-5204-4fa0-add3-603d636d7672)


   - Forgot Password page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-forgot-2024-02-04-05_23_20](https://github.com/caleb1711/blog-institue/assets/130179631/a4d6e1dc-cee6-4eef-b67f-44c2117d7952)


   - Reset Password page mobile view
   
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-accounts-reset-6e556103-aced-4f68-a3b7-4a0a7242dc7a-2024-02-04-05_24_22](https://github.com/caleb1711/blog-institue/assets/130179631/dc972f19-3792-4a48-a5aa-b1aa2def1765)


   - My Blogs page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-myblogs-2024-02-04-05_25_35](https://github.com/caleb1711/blog-institue/assets/130179631/eb414171-c312-493b-96a8-048f3cc24602)


   - Add Blog page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-addblog-2024-02-04-05_27_49](https://github.com/caleb1711/blog-institue/assets/130179631/8dc56eae-a310-40c3-ac9f-5dbae138abee)


   - Edit Blog page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-editblog-15-2024-02-04-05_27_13](https://github.com/caleb1711/blog-institue/assets/130179631/98bba520-dce8-4583-9881-9859057dca00)


   - About Us page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-about-2024-02-04-05_30_28](https://github.com/caleb1711/blog-institue/assets/130179631/b7617fe1-fa2a-4e15-bc29-f1c25992ed19)


   - Contact Us page mobile view

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-contact-2024-02-04-05_30_59](https://github.com/caleb1711/blog-institue/assets/130179631/a4f6cd77-eab1-44b7-8ede-92f614431e19)


   - Privacy Policy
  
   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-privacy-2024-02-04-05_31_24](https://github.com/caleb1711/blog-institue/assets/130179631/ffd88c9f-542a-40f6-99fb-ccb596e9af6e)

   - Term's & Conditions

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-terms-2024-02-04-05_32_06](https://github.com/caleb1711/blog-institue/assets/130179631/b6644c5c-8f3e-410c-b02d-58a52cea9591)


   - Disclaimer

   ![screencapture-blog-institutes-a9fd3e1b31a5-herokuapp-disclaimer-2024-02-04-05_32_46](https://github.com/caleb1711/blog-institue/assets/130179631/da8bbcb0-338b-46d8-8f88-bbeb51bbdf37)


## Features

### Authentication System

- **User Registration:** Allow users to create accounts and register on the platform.
- **User Login:** Provide secure user authentication with login functionality.
- **Password Reset:** Enable users to reset their passwords in case of forgetfulness.

### Blog CRUD Operations

- **Create Blog Posts:** Authenticated users can create new blog posts with a title, content, and optional images.
- **Read Blog Posts:** Display a list of blog posts, and users can view the details of each post individually.
- **Update Blog Posts:** Allow authors to edit and update their existing blog posts.
- **Delete Blog Posts:** Provide an option to delete blog posts for authorized users.

### Security Features

Blogs Institute prioritizes security to protect user data and ensure a safe environment for both bloggers and readers. The following security features are implemented:

- **CSRF Protection:**
  - Cross-Site Request Forgery (CSRF) protection is implemented to prevent unauthorized third-party sites from making malicious requests on behalf of a user. Django provides built-in CSRF protection by generating and validating unique tokens for each form submission.

- **Password Hashing:**
  - User passwords are stored securely using strong cryptographic hashing. Django automatically uses a secure password hashing algorithm to hash and salt user passwords. This ensures that even if the database is compromised, passwords remain protected.

- **User Authentication:**
  - Django's authentication system is used to manage user sessions and authenticate users securely. It includes features like session-based authentication and cookie-based authentication, making it resistant to common attacks like session hijacking.

- **Authorization and Permissions:**
  - User permissions are strictly enforced to control access to different parts of the application. Only authenticated and authorized users have access to perform CRUD operations on blog posts. Django's built-in permission system is leveraged to define and enforce authorization rules.

- **HTTPS Protocol:**
  - Blogs Institute enforces the use of the HTTPS protocol to secure data transmitted between the user's browser and the server. This ensures the confidentiality and integrity of user data during transit.

- **Content Security Policy (CSP):**
  - A Content Security Policy is implemented to mitigate the risk of cross-site scripting (XSS) attacks. CSP helps prevent the execution of malicious scripts by defining a whitelist of trusted sources for content, scripts, and other resources.

- **Database Security:**
  - Django employs database security measures to protect against SQL injection attacks. Query parameters and prepared statements are used to ensure that user inputs are sanitized before interacting with the database.

- **Django Security Updates:**
  - Regularly updating Django to the latest version is encouraged to benefit from the latest security patches and enhancements. This helps to address any vulnerabilities that may be discovered in the framework.

- **Security Headers:**
  - Appropriate security headers, such as Strict-Transport-Security (HSTS) and X-Content-Type-Options, are set to enhance the overall security posture of the application.


 
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


# Data Schema and Relationships

This section provides an overview of the data schema and relationships within the Blogs Institute Django application.

## Data Models

### 1. User Model (Customized from `AbstractUser`)

Represents user information within the application.

- Fields:
  - `id`: Primary key
  - `email`: User's email address (unique)
  - `forgot_email_token`: Token for email-related operations (null and blank allowed)
  - `USERNAME_FIELD`: Set to 'email' for authentication
  - `REQUIRED_FIELDS`: Empty list to make email the only required field
  - `objects`: Custom user manager for querying users by email
  - `created_at`: Date and time when the user was created
  - `updated_at`: Date and time when the user was last updated

### 2. Blog Model

Represents individual blog posts created by users.

- Fields:
  - `id`: Primary key
  - `user`: Foreign key to the `User` model, indicating the owner of the blog
  - `image`: Image associated with the blog post
  - `title`: Title of the blog post
  - `content`: Main content of the blog post
  - `upvotes`: Number of upvotes for the blog post
  - `downvotes`: Number of downvotes for the blog post
  - `created_at`: Date and time when the blog post was created
  - `updated_at`: Date and time when the blog post was last updated

### 3. Comment Model

Represents comments made by users on blog posts.

- Fields:
  - `id`: Primary key
  - `user`: Foreign key to the `User` model, indicating the user who made the comment
  - `blog`: Foreign key to the `Blog` model, indicating the blog post being commented on
  - `content`: Main content of the comment
  - `created_at`: Date and time when the comment was created
  - `updated_at`: Date and time when the comment was last updated

## Relationships

### User to Blog Relationship

- **Type:** One-to-Many
- **Description:** Each user can create multiple blog posts, but each blog post is associated with only one user.
- **Implementation:**
  - The `user` field in the `Blog` model is a foreign key that references the `User` model.

### User to Comment Relationship

- **Type:** One-to-Many
- **Description:** Each user can create multiple comments, but each comment is associated with only one user.
- **Implementation:**
  - The `user` field in the `Comment` model is a foreign key that references the `User` model.

### Blog to Comment Relationship

- **Type:** One-to-Many
- **Description:** Each blog post can have multiple comments, but each comment is associated with only one blog post.
- **Implementation:**
  - The `blog` field in the `Comment` model is a foreign key that references the `Blog` model.

## Database Schema

Below is a simplified representation of the database schema:

```plaintext
User
| id | email           | forgot_email_token | created_at           | updated_at           |
|----|-----------------|--------------------|----------------------|----------------------|
| 1  | john@example.com| some_token         | 2023-01-01T12:00:00Z | 2023-01-01T12:00:00Z |

Blog
| id | user_id | image                | title       | content                | upvotes | downvotes | created_at           | updated_at           |
|----|---------|----------------------|-------------|------------------------|---------|-----------|----------------------|----------------------|
| 1  | 1       | blog_images/1.jpg    | First Post  | This is the first post | 10      | 2         | 2023-01-02T10:30:00Z | 2023-01-02T10:30:00Z |
| 2  | 1       | blog_images/2.jpg    | Second Post | Another interesting... | 5       | 0         | 2023-01-03T08:45:00Z | 2023-01-03T08:45:00Z |

Comment
| id | user_id | blog_id | content                   | created_at           | updated_at           |
|----|---------|---------|---------------------------|----------------------|----------------------|
| 1  | 1       | 1       | Great post!               | 2023-01-02T11:00:00Z | 2023-01-02T11:00:00Z |
| 2  | 1       | 1       | I agree with your points! | 2023-01-02T11:15:00Z | 2023-01-02T11:15:00Z |
```


## Continuous Integration and Testing

- The project follows best practices for continuous integration and testing to ensure code quality and reliability. Key points in this process include:

### Automated Testing


1. **Directory Structure:**
   - Organize your tests within the `tests` directory in your Django app.

### Test Classes

2. **Use Django's `TestCase`:**
   - Utilize Django's `TestCase` class for  test classes.

### Descriptive Naming

3. **Naming Conventions:**
   - Choose descriptive names for your test classes and methods. Follow a naming convention such as `TestAddBlog`.

### Test Fixtures

4. **Fixture Setup:**
   - Create necessary fixtures or use Django's `setUp` method to set up test data.

### Use Appropriate Assertions

5. **Django TestCase Assertions:**
   - When writing tests for  Django application, utilize assertions provided by the Django `TestCase` class. Common assertions include:
     - `assertEqual(a, b)`: Check if `a` and `b` are equal.
     - `assertNotEqual(a, b)`: Check if `a` and `b` are not equal.
     - `assertTrue(x)`: Check if `x` is `True`.
     - `assertFalse(x)`: Check if `x` is `False`.
     - `assertRaises(exception, callable, *args, **kwargs)`: Check if calling `callable(*args, **kwargs)` raises the specified exception.
     - ... and more.

   - Refer to the [Django TestCase documentation](https://docs.djangoproject.com/en/stable/topics/testing/tools/#django.test.TestCase) for a comprehensive list of assertions available.

   - Example:
     ```python
     from django.test import TestCase

     class YourTestCase(TestCase):
         def test_example(self):
             value = 42
             self.assertEqual(value, 42, "The value should be 42")
           

### Comprehensive Coverage

6. **Cover Critical Paths:**
   - Aim for comprehensive test coverage, ensuring that critical code paths are tested thoroughly.

### Isolation

7. **Test Isolation:**
   - Ensure each test is isolated and does not depend on the state left behind by other tests.

## Running Tests

To run tests for the blog institute Django application, execute the following command:

```bash
python manage.py test accounts
python manage.py test blog
```

- __VALIDATOR TESTING__
   - VALIDATOR TESTING with wc3 of all the front end .
   - Python testing done is manually
   - Django testing done manually
   - All the features of our Project is Done
    ![20](https://github.com/caleb1711/blog-institue/assets/130179631/809e85c1-8680-4e6f-b556-a491eda53e06)



## DEPLOYMENT

This section provides step-by-step instructions on how to deploy the Blogs Institute Django application on Heroku. 

### Prerequisites

Before you begin, make sure you have the following:

- A [Heroku account](https://signup.heroku.com/) .
- [Git](https://git-scm.com/) installed on your local machine.
- The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

### Deployment Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/caleb1711/blog-institue.git
   cd blogs-institute

   heroku create blog

   heroku config:set SECRET_KEY='your_secret_key'
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=*
   heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   heroku config:set EMAIL_HOST=smtp.gmail.com
   heroku config:set EMAIL_PORT=port
   heroku config:set EMAIL_USE_TLS=True
   heroku config:set EMAIL_USE_SSL=False 
   heroku config:set EMAIL_HOST_USER=hostemsail  
   heroku config:set EMAIL_HOST_PASSWORD=password
   heroku config:set DEFAULT_FROM_EMAIL=Blog Institute <email>

   git push heroku main

   heroku run python manage.py migrate

   heroku run python manage.py createsuperuser

   heroku open

- Make sure to set the ALLOWED_HOSTS environment variable on Heroku to the domain name of your app.
- I also enable the the automatic deployments with main branch.

## Acknowledgments

We would like to extend our appreciation to the following individuals and resources that have contributed to the development and success of Blogs Institute:

- **Bootstrap and Roboto Fonts**: Special thanks to the Bootstrap framework and Roboto font family for enhancing the visual design and responsiveness of our website.

- **Django**: A big shoutout to the Django framework for powering the backend of our blogging platform.

- **GitHub**: Our project is hosted on GitHub, providing a collaborative and version-controlled environment.


These contributions have played a crucial role in shaping Blogs Institute, and we want to express our sincere thanks to everyone involved.


## Authors

- Calkra15@outlook.com

## Contact

If you have any questions or need support, you can reach me at Calkra15@outlook.com.
