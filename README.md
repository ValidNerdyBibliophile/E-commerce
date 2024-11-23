
# E-Commerce Backend API using Django

This is the backend API for an e-commerce platform built using Django and Django Rest Framework (DRF). It handles user management, authentication, and various operations related to user accounts.

## Features

- **User Management**: Create, read, update, and delete user details.
- **Authentication**: Login and password management.
- **Search**: Endpoint to search for users.
- **Custom User Model**: Uses a custom user model for more flexibility.

## Setup

Follow the steps below to set up the project locally.

### Prerequisites

- Python 3.8 or higher
- MySQL Database (you can use other databases as well, but MySQL is preferred for this project)
- Django 5.1.3 or later
- Django Rest Framework (DRF)
- Elasticsearch (for search functionality, if implemented)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/ValidNerdyBibliophile/E-commerce.git
   cd E-commerce
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .env
   source .env/bin/activate  # On Windows, use .env\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up db variables:

   Create a `~/.ecommerce_config.json` file

   ```json
    {
    "DB_NAME": "database_name",
    "DB_USER": "db_user",
    "DB_PASSWORD": "db_password",
    "DB_HOST": "localhost",
    "DB_PORT": "3306"
    }
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   cd ecommerce
   python manage.py runserver
   ```

   The server will be available at `http://127.0.0.1:8000/`.

### API Endpoints

The following API endpoints are available:

#### 1. **Create User**
- **Endpoint**: `POST /api/accounts/`
- **Request Body**: 
  ```json
  {
    "username": "testuser",
    "password": "password123",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User",
    "is_active": true,
    "is_staff": false
  }
  ```

#### 2. **List Users**
- **Endpoint**: `GET /api/accounts/`
- **Response**: A list of all users with basic details.

#### 3. **Retrieve User Details (By ID or Username)**
- **Endpoint**: `GET /api/accounts/{id_or_username}/`
- **Response**:
  ```json
  {
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com",
    "is_active": true
  }
  ```

#### 4. **Update User Details**
- **Endpoint**: `PUT /api/accounts/{id_or_username}/`
- **Request Body** (Example):
  ```json
  {
    "email": "newemail@example.com",
    "first_name": "Updated",
    "last_name": "User"
  }
  ```
- **Response**:
  ```json
  {
    "detail": "User details updated successfully.",
    "updated_fields": {
      "email": "newemail@example.com",
      "first_name": "Updated",
      "last_name": "User"
    }
  }
  ```

#### 5. **Delete User (By ID or Username)**
- **Endpoint**: `DELETE /api/accounts/{id_or_username}/`
- **Response**:
  ```json
  {
    "detail": "User 'testuser' deleted successfully."
  }
  ```

### Authentication

- **Login**: You can authenticate users by implementing a login API (though not yet included in this project).
- **Password Reset**: You can add password reset functionality by creating custom views and serializers for password reset functionality.

### Testing

You can test the APIs using tools like [Postman](https://www.postman.com/) or directly via the browser for `GET` requests.

#### Testing User Creation (Postman)
1. Set the method to `POST`.
2. Use the endpoint `http://127.0.0.1:8000/api/accounts/`.
3. Add a JSON body with the required user details (e.g., username, email, password).

### Testing User List (Postmane)
1. Set the method to `GET`.
2. Use the endpoint `http://127.0.0.1:8000/api/accounts/list/`.

### Retrieve user details using ID or usermane
1. Set the method to `GET`.
2. Use the endpoint `http://localhost:8000/api/accounts/{id_or_username}/`.

#### Testing User Update (Postman)
1. Set the method to `PUT`.
2. Use the endpoint `http://127.0.0.1:8000/api/accounts/{id_or_username}/`.
3. Add the fields you want to update in the JSON body.

#### Testing User Deletion (Postman)
1. Set the method to `DELETE`.
2. Use the endpoint `http://127.0.0.1:8000/api/accounts/{id_or_username}/`.

### Future Enhancements

- **User Login**: Implement JWT or Session-based login for authentication.
- **Password Reset**: Add password reset functionality for users who forget their password.
- **Elasticsearch Integration**: For product search functionality.
- **Login**: User authentication with password decryption, cookies (expires after 30 minutes), and CSRF tokens.
- **Search**: Implement Elasticsearch for product search with paging, sorting, and filters.
- **Cart**: Add cart management features, including adding items to the cart, updating cart items, and deleting them.
- **Payment Integration**: Integrate with open APIs for payment processing.
- **Checkout**: Implement the checkout process to handle orders.
- **Front end Integration**: Implement a UI and integrate it with the backend.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License