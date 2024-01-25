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
