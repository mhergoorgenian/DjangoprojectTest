# Django REST Framework Authentication API

This project provides RESTful API endpoints for user authentication and profile management.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install django djangorestframework
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- **Register**: `POST /api/users/register/`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "securepassword123",
      "password2": "securepassword123",
      "first_name": "Test",
      "last_name": "User"
    }
    ```
  - Response:
    ```json
    {
      "token": "your-auth-token",
      "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
      }
    }
    ```

- **Login**: `POST /api/users/login/`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "securepassword123"
    }
    ```
  - Response:
    ```json
    {
      "token": "your-auth-token",
      "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
      }
    }
    ```

- **Logout**: `POST /api/users/logout/`
  - Headers:
    ```
    Authorization: Token your-auth-token
    ```
  - Response: 204 No Content

### User Profile

- **Get User Profile**: `GET /api/users/profile/`
  - Headers:
    ```
    Authorization: Token your-auth-token
    ```
  - Response:
    ```json
    {
      "id": 1,
      "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
      },
      "bio": "My bio",
      "location": "New York",
      "birth_date": "1990-01-01",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
    ```

- **Update User Profile**: `PUT /api/users/profile/`
  - Headers:
    ```
    Authorization: Token your-auth-token
    ```
  - Request Body:
    ```json
    {
      "bio": "Updated bio",
      "location": "Los Angeles",
      "birth_date": "1990-01-01"
    }
    ```
  - Response: Updated profile object

- **Get User Data**: `GET /api/users/me/`
  - Headers:
    ```
    Authorization: Token your-auth-token
    ```
  - Response:
    ```json
    {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "first_name": "Test",
      "last_name": "User"
    }
    ``` 