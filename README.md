# Django Advanced Topics  

A repository dedicated to exploring and implementing advanced Django concepts and features. This project demonstrates the use of modern tools, libraries, and techniques to build robust and efficient Django applications.

---

## Features  

- **NinjaAPI Integration**:  
  - High-performance API development with Django Ninja.  
  - Built-in support for data validation and OpenAPI documentation.  

- **GraphQL**:  
  - Implementation of GraphQL queries and mutations for efficient data retrieval.  

- **Custom Middleware**:  
  - Enhance request and response handling by creating and utilizing custom middleware.  

- **Comprehensive CRUD Operations**:  
  - Demonstrates CRUD functionality with Django Ninja and Django Rest Framework.  

- **Branching for Focused Development**:  
  - **`django_ninja` branch**: Contains implementations and examples focused solely on Django Ninja.  

---

## Technologies Used  

- **Backend Framework**: Django  
- **API Development**: Django Ninja, GraphQL  
- **Documentation**: Swagger/OpenAPI  
- **Database**: PostgreSQL  
- **Other Tools**: Docker, Git  

---

## Repository Structure  

```plaintext  
django-advanced_topics/  
│  
├── core/  
│   ├── models.py         # Core database models  
│   ├── serializers.py    # Serializers for API integration  
│   ├── views.py          # Views for handling API requests  
│   ├── urls.py           # URL routing configuration  
│  
├── ninja/  
│   ├── api.py            # NinjaAPI setup and endpoints  
│   ├── routers.py        # Router configuration for NinjaAPI  
│  
├── graphql/  
│   ├── schema.py         # GraphQL schema definitions  
│   ├── queries.py        # GraphQL queries  
│   ├── mutations.py      # GraphQL mutations  
│  
├── middleware/  
│   ├── custom_middleware.py # Custom middleware examples  
│  
├── Dockerfile            # Docker configuration for containerized deployment  
├── README.md             # Project documentation  
```  

---

## Setup and Installation  

### Prerequisites  

- Python 3.9+  
- PostgreSQL  
- Docker (optional, for containerized deployment)  

### Installation Steps  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/Mohamed-Taha-Essa/django-advanced_topics.git  
   cd django-advanced_topics  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run Migrations**:  
   ```bash  
   python manage.py migrate  
   ```  

4. **Start the Development Server**:  
   ```bash  
   python manage.py runserver  
   ```  

5. **Access the API Documentation**:  
   - NinjaAPI docs: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)  

---

## Branch Details  

- **`main`**: Contains the core implementation and features.  
- **`django_ninja`**: Dedicated branch for Django Ninja API examples and use cases.  

---

## Contribution  

Contributions are welcome! Please follow these steps:  

1. Fork the repository.  
2. Create a new branch (`feature/your-feature-name`).  
3. Commit your changes.  
4. Push to the branch.  
5. Open a pull request.  

---

## License  

This project is licensed under the MIT License.  

---

## Contact  

For any inquiries or feedback, please contact:  
**Mohamed Taha Essa**  
[GitHub Profile](https://github.com/Mohamed-Taha-Essa)  
