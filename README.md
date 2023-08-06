# LittleLemon Capstone Project - Django API Documentation

## Introduction

LittleLemon Capstone Project is a Django web application developed to manage the Little Lemon Restaurant operations. The app provides interfaces to manage menu items, bookings, user registration, and authentication.


## Prerequisites

Ensure you have Python installed on your system. If not, download and install Python from the official [Python website](https://www.python.org/downloads/).

## Setting Up a Virtual Environment

### For macOS:

1. **Navigate to the project directory**

   Open the terminal and navigate to the "LittleLemon" project directory.
  
2. **Activate the virtual environment**

   ```bash
   source littlelemon_env/bin/activate
   ```
### For Windows:

1. **Navigate to the project directory**

   Open the Command Prompt or PowerShell and navigate to the "LittleLemon" project directory.

2. **Activate the virtual environment**

   If using Command Prompt:
   
   ```bash
   .\littlelemon_env\Scripts\activate
   ```
    If using PowerShell:

   ```bash
   .\littlelemon_env\Scripts\Activate.ps1
   ```

## Models

### 1. Menu

- **Title**: CharField (255 characters max)
- **Price**: DecimalField (2 decimal places)
- **Inventory**: IntegerField

### 2. Booking

- **Name**: CharField (255 characters max)
- **No_of_guests**: IntegerField
- **Bookingdate**: DateTimeField
  

## API Paths for Testing

### 1. Menu Items

**URL**: `/restaurant/menu/`

- **Method**: `GET` - Retrieves the list of all menu items.
- **Method**: `POST` 
  - Creates a new menu item.
  - **Sample Body**:

```json
{
    "Title": "Dish Name",
    "Price": 12.50,
    "Inventory": 10
}
```

**URL**: `/restaurant/menu/<int:pk>/`

- **Method**: `GET` - Retrieves details of a specific menu item by its ID.
- **Method**: `PUT` - Updates a specific menu item by its ID.
- **Method**: `DELETE` - Deletes a specific menu item by its ID.

### 2. Bookings

**URL**: `/restaurant/bookings/`

Uses Django REST framework's default router, supporting multiple CRUD operations. Kindly refer to DRF's documentation for CRUD operations.

### 3. User Authentication

**URL**: `/token-auth/`

- **Method**: `POST`
- Obtain an authentication token.
- **Sample Body**:
  
```json
{
    "username": "your_username",
    "password": "your_password"
}
```


## Setting up the Project on a New Machine

1. Clone the Git repository to your local machine.
2. Navigate to the project root directory.
3. Install required packages:
   
```bash
pip install -r requirements.txt
```

4. Set up the MySQL database with the name `LittleLemon`. Update the `DATABASES` configuration in `settings.py` with your MySQL credentials.
5. Run migrations:
   
```bash
python manage.py migrate
```

6. Start the Django development server:

```bash
python manage.py runserver
```

## Review Criteria

1. **Static HTML Content**: The web application uses Django to serve static HTML content. Check the `index.html` located in the templates directory which includes the restaurant logo served statically.
2. **Git Repository**: Ensure you've committed the project to a Git repository and shared the link.
3. **MySQL Database**: The application connects to a MySQL database as seen in the `DATABASES` configuration in `settings.py`.
4. **APIs Implementation**: The application includes APIs for menu items and table bookings. You can test these APIs with provided paths.
5. **User Registration & Authentication**: The app is integrated with the `djoser` library for user registration and authentication. The URLs for these operations can be found under the `/auth/` path.
6. **Unit Tests**: [Awaiting code for the unit tests]
7. **Testing with Insomnia**: All APIs can be tested using the Insomnia REST client by sending requests to the provided API paths.



















