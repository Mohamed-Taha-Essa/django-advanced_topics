
# book_advanced_topics

A repository designed to explore and apply advanced Django concepts, focusing on **Django Ninja** for creating high-performance APIs.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)

## Overview
This branch of `book_advanced_topics` is dedicated to building APIs using **Django Ninja**. The project showcases CRUD operations and filters implemented with Django Ninja’s efficient, async-friendly API framework.

## Features
- **CRUD Operations**: Implemented using Django Ninja.
- **Advanced API Functionality**: Built entirely with Django Ninja.
- **Fast and Scalable**: Designed with performance in mind for production-grade applications.

## Technologies Used
- **Django**: Web framework for Python.
- **Django Ninja**: High-performance web framework for building APIs.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/book_advanced_topics.git
   cd book_advanced_topics
   git checkout django_ninja
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/api/docs` to explore available endpoints.

## API Documentation

The following endpoints manage `Book` resources in the **book_advanced_topics** API.

#### 1. List All Books
- **Endpoint**: `GET /api/`
- **Description**: Retrieve a list of books with optional filters.
- **Response**: `200 OK` - Returns a list of books matching the filters.
- **Parameters**:
  - `filters`: Use the `BookFilterSchema` to filter the books list.
- **Example Request**: `/api/`

#### 2. Get Book Details
- **Endpoint**: `GET /api/{book_id}`
- **Description**: Retrieve details of a specific book by its ID.
- **Response**: `200 OK` - Returns the details of the specified book.
- **Parameters**:
  - `book_id`: The unique ID of the book to retrieve.
- **Example Request**: `/api/1`

#### 3. Create a New Book
- **Endpoint**: `POST /api/`
- **Description**: Add a new book to the database.
- **Response**: `200 OK` - Returns the created book’s details.
- **Payload**:
  - `title`: Title of the book.
  - `author`: ID of the author (must exist).
  - `category`: ID of the category (must exist).
  - `publication_date`: Publication date of the book.
  - `price`: Price of the book.
  - `description`: Description of the book.
  - `quantity`: Quantity of the book in stock.
- **Example Payload**:
  ```json
  {
    "title": "New Book Title",
    "author": 1,
    "category": 2,
    "publication_date": "2024-11-01",
    "price": 19.99,
    "description": "A detailed book description.",
    "quantity": 10
  }
  ```

#### 4. Update a Book
- **Endpoint**: `PUT /api/{book_id}`
- **Description**: Update details of an existing book.
- **Response**: `200 OK` - Returns the updated book’s details.
- **Parameters**:
  - `book_id`: The unique ID of the book to update.
- **Payload**: Same as the **Create a New Book** endpoint.
- **Example Request**: `/api/1`

#### 5. Delete a Book
- **Endpoint**: `DELETE /api/{book_id}`
- **Description**: Delete a book from the database.
- **Response**: `200 OK` - Returns a message indicating successful deletion.
- **Parameters**:
  - `book_id`: The unique ID of the book to delete.
- **Example Request**: `/api/1`

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

---

This README provides focused documentation for the Django Ninja API functionality in the `django_ninja` branch.