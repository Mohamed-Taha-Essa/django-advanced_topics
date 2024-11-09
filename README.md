
# Book Management GraphQL API

This project implements a Book Management system using Django and GraphQL. The API allows users to perform CRUD operations on books, query detailed information about books and authors, and apply custom filters such as title, description, price range, and pagination.

## Features

- **Fetch List of Books**: Query a list of books with filtering options.
- **Fetch Detailed Book Information**: Query detailed information about a specific book by ID.
- **Fetch All Authors**: Query a list of all authors.
- **Fetch Reviews for a Book**: Query the reviews associated with a specific book.
- **CRUD Operations on Books**: Create, Update, and Delete books via mutations.
- **Custom Filtering**: Filter books by title, description, and price range (minPrice and maxPrice).
- **Pagination**: Paginate the results of book queries.

## Requirements

- Python 3.8+
- Django 5.x+
- Graphene-Django
- django-filter


## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Apply Migrations

```bash
python manage.py migrate
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

### 4. Access the GraphQL Playground

Once the server is running, you can access the GraphQL Playground at `http://127.0.0.1:8000/graphql/` to interact with the GraphQL API.

## API Endpoints

### Queries

- **List of Books**:

  To fetch a list of books, use the following query:

  ```graphql
  query {
    allBooks(first: 10, minPrice: 10, maxPrice: 50) {
      edges {
        node {
          id
          title
          description
          price
          author {
            name
          }
          category {
            name
          }
        }
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
  ```

  - `first: 10` - Fetches the first 10 books.
  - `minPrice: 10` - Filters books with a price greater than or equal to 10.
  - `maxPrice: 50` - Filters books with a price less than or equal to 50.
  - Pagination is applied with `pageInfo`, `endCursor`, and `hasNextPage`.

- **Detailed Book Information**:

  To fetch details of a specific book by ID, use this query:

  ```graphql
  query {
    book(id: 1) {
      id
      title
      description
      price
      publicationDate
      author {
        name
      }
      category {
        name
      }
      review {
        id
        rating
        comment
      }
    }
  }
  ```

- **List of All Authors**:

  To fetch a list of authors, use:

  ```graphql
  query {
    authors {
      id
      name
    }
  }
  ```

### Mutations

#### Create Book

To create a new book, use the following mutation:

```graphql
mutation {
  createBook(input: {
    title: "New Book"
    author: 1
    category: 2
    description: "This is a new book"
    price: 25.99
    publicationDate: "2024-01-01"
  }) {
    success
    book {
      id
      title
      author {
        name
      }
      category {
        name
      }
    }
  }
}
```

#### Update Book

To update an existing book, use this mutation:

```graphql
mutation {
  updateBook(input: {
    id: 1
    title: "Updated Book Title"
    description: "Updated description"
    price: 30.99
    publicationDate: "2024-06-01"
  }) {
    success
    book {
      id
      title
      description
      price
      publicationDate
    }
  }
}
```

#### Delete Book

To delete an existing book, use this mutation:

```graphql
mutation {
  deleteBook(id: 1) {
    success
  }
}
```

### Filtering and Pagination

You can filter the books by using the following custom filter fields:

- **title**: Search for books with a title that contains the specified string (`icontains`).
- **description**: Search for books with a description that contains the specified string (`icontains`).
- **minPrice**: Filter books with a price greater than or equal to the provided value.
- **maxPrice**: Filter books with a price less than or equal to the provided value.

#### Example: Custom Filtering and Pagination

```graphql
query {
  allBooks(first: 10, minPrice: 15, maxPrice: 50, title: "Graphene") {
    edges {
      node {
        id
        title
        description
        price
        author {
          name
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
```

- This query fetches the first 10 books whose title contains "Graphene" and whose price is between 15 and 50.

## Models

- **Book**: Represents a book with fields such as `title`, `description`, `price`, `author`, `category`, and `publicationDate`.
- **Author**: Represents an author, with fields like `name`.
- **Category**: Represents a category for books.
- **Review**: Represents a review for a book, containing fields such as `rating`, `comment`, and a reference to the `Book`.

## Filtering and Pagination

We are using `graphene-django` and `django-filter` for filtering and pagination.

- **Filtering**: The `BookFilter` class is used to filter the books by `title`, `description`, and `price`. You can filter books based on `minPrice` and `maxPrice` using `gte` (greater than or equal) and `lte` (less than or equal).
  
- **Pagination**: We use `DjangoFilterConnectionField` to handle pagination for the `all_books` query. It automatically adds pagination support with arguments like `first`, `last`, `before`, and `after`.

## Conclusion

This GraphQL API provides a comprehensive solution for managing books, authors, categories, and reviews. It supports filtering, pagination, and CRUD operations for books, making it a flexible tool for managing a book inventory system.