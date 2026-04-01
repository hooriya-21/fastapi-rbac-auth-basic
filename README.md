# FastAPI Role-Based Authentication

## Features
- JWT Authentication
- Role-Based Access Control (RBAC)
- Admin and User APIs

## Endpoints
- POST /login
- GET /admin-data
- GET /user-data

## How it works
1. User logs in and gets JWT token
2. Token contains role
3. APIs are protected based on role
# Login API - verifies user and returns JWT token
# Role-based dependency to restrict access
## Future Improvements
- Password hashing
- Token expiration
- Database integration
