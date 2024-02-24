# Sumadhura_task

# Vehicle Management System

## Overview
The Vehicle Management System is a Django-based application designed to manage vehicles, vendors, products, and quality checks associated with vehicles. It provides APIs for registration, login, managing vendors, products, vehicles, quality checks, and vehicle checkouts.

## Features
- User Registration: Users can register with the system to access its features.
- User Authentication: Registered users can log in to the system securely using authentication tokens.
- Vendor Management: CRUD operations for managing vendors who supply vehicles or products.
- Product Management: CRUD operations for managing products associated with vehicles.
- Vehicle Management: CRUD operations for managing vehicles, including vehicle details, checkout status, and associated vendors and products.
- Quality Check: Perform quality checks on vehicles to determine whether they passed or failed.
- Vehicle Checkout: Mark vehicles as checked out.
- API Endpoints: Provides RESTful APIs for all CRUD operations and additional features.

## API Endpoints
- `/login/`: POST request to obtain an authentication token for logging in.
- `/register/`: POST request to register a new user.
- `/logout/`: POST request to log out and invalidate the authentication token.
- `/vendors/`: GET request to list all vendors and POST request to create a new vendor.
- `/products/`: GET request to list all products and POST request to create a new product.
- `/vehicles/`: GET request to list all vehicles and POST request to create a new vehicle.
- `/qualitychecks/`: GET request to list all quality checks and POST request to perform a quality check.
- `/vehicles/<int:pk>/`: GET request to retrieve details of a specific vehicle, PUT request to update vehicle details, DELETE request to delete a vehicle.
- `/vehicles/<int:pk>/checkout/`: POST request to mark a vehicle as checked out.

## Technologies Used
- Django: Web framework for building the application.
- Django REST Framework: Toolkit for building Web APIs in Django.
- MySQL: Database management system for storing application data.
- Django REST Framework Token Authentication: Token-based authentication for API endpoints.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install Python and pip if not already installed.
3. Install dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
4. Set up a MySQL database and update the database configuration in `settings.py`.
5. Run database migrations using `python manage.py migrate`.
6. Start the Django development server using `python manage.py runserver`.