# Wallet Saver API

A professional FastAPI application for managing transactions and categories with JWT authentication, PostgreSQL database, and Alembic migrations.

## Features

- **JWT Authentication**: Secure user registration and login system
- **Transaction Management**: Create, read, update, and delete transactions
- **Category Management**: Organize transactions with custom categories
- **PostgreSQL Database**: Robust database with SQLAlchemy ORM
- **Alembic Migrations**: Database schema version control
- **Professional Structure**: Clean, scalable codebase architecture

## Project Structure

```
windsurf-project/
|
app/
|   api/
|   |   auth.py          # Authentication endpoints
|   |   categories.py    # Category CRUD endpoints
|   |   transactions.py # Transaction CRUD endpoints
|   |
|   core/
|   |   config.py       # Application configuration
|   |   security.py     # JWT and password utilities
|   |
|   db/
|   |   database.py     # Database connection setup
|   |   session.py      # Database session management
|   |
|   models/
|   |   user.py         # User model
|   |   category.py     # Category model
|   |   transaction.py  # Transaction model
|   |
|   schemas/
|   |   user.py         # User Pydantic schemas
|   |   category.py     # Category Pydantic schemas
|   |   transaction.py  # Transaction Pydantic schemas
|   |
|   services/
|   |   auth.py         # Authentication business logic
|   |
|   main.py             # FastAPI application entry point
|
alembic/                # Database migrations
requirements.txt        # Python dependencies
.env                    # Environment variables
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip or pip3

### Installation

1. **Clone the repository** (if applicable)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database**:
   ```sql
   CREATE DATABASE walletsaver_db;
   CREATE USER user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE walletsaver_db TO user;
   ```

4. **Configure environment variables**:
   Copy `.env` file and update the values:
   ```bash
   cp .env.example .env
   ```
   
   Update the `.env` file with your actual database credentials:
   ```
   DATABASE_URL=postgresql://user:password@localhost/walletsaver_db
   SECRET_KEY=your-super-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

### Running the Application

1. **Start the FastAPI server**:
   ```bash
   python app/main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the API**:
   - API Documentation: http://localhost:8000/docs
   - Alternative Documentation: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/health

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/token` - Login and get access token
- `GET /auth/me` - Get current user information

### Categories
- `POST /categories/` - Create a new category
- `GET /categories/` - Get all categories for current user
- `GET /categories/{category_id}` - Get specific category
- `PUT /categories/{category_id}` - Update category
- `DELETE /categories/{category_id}` - Delete category (soft delete)

### Transactions
- `POST /transactions/` - Create a new transaction
- `GET /transactions/` - Get all transactions for current user
- `GET /transactions/{transaction_id}` - Get specific transaction
- `PUT /transactions/{transaction_id}` - Update transaction
- `DELETE /transactions/{transaction_id}` - Delete transaction (soft delete)

## Usage Examples

### Register a new user
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

### Login and get token
```bash
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=securepassword123"
```

### Create a category (with token)
```bash
curl -X POST "http://localhost:8000/categories/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Groceries",
    "description": "Food and household items",
    "color": "#FF5733"
  }'
```

### Create a transaction (with token)
```bash
curl -X POST "http://localhost:8000/transactions/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50.75,
    "description": "Weekly groceries",
    "type": "expense",
    "date": "2023-12-01T10:00:00",
    "category_id": 1
  }'
```

## Database Migrations

### Create a new migration
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback migrations
```bash
alembic downgrade -1
```

## Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Secure authentication with configurable expiration
- **User Isolation**: Users can only access their own data
- **Input Validation**: Pydantic models for request/response validation
- **Soft Deletes**: Data is marked as deleted rather than permanently removed

## Development

### Adding New Features

1. **Models**: Add new SQLAlchemy models in `app/models/`
2. **Schemas**: Create Pydantic schemas in `app/schemas/`
3. **Endpoints**: Implement API endpoints in `app/api/`
4. **Services**: Add business logic in `app/services/`

### Testing

The project structure supports adding tests in a `tests/` directory. Consider using pytest for testing.

## Production Considerations

- Update the `SECRET_KEY` in production
- Configure proper CORS origins instead of allowing all origins
- Use environment-specific database credentials
- Set up proper logging and monitoring
- Consider using HTTPS in production
- Implement rate limiting for API endpoints

## License

This project is provided as-is for educational and development purposes.
