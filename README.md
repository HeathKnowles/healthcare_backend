# Healthcare Backend

## Workflow

1) Set environment variables
- Copy the template from [.env.example](.env.example) to .env and fill in your PostgreSQL and Django settings.

2) Install dependencies
- Use your Python environment and install project dependencies (Django, DRF, SimpleJWT, psycopg2, python-dotenv).

3) Run migrations
- python manage.py makemigrations
- python manage.py migrate

4) Start the server
- python manage.py runserver

5) Test with Postman
- Register: POST /api/auth/register/
- Login: POST /api/auth/login/ (use email as username)
- Use the access token as a Bearer token for all other endpoints.
- Test patients, doctors, and mappings endpoints.

## Postman Collection

Import [postman_collection.json](postman_collection.json) into Postman for pre-configured requests covering:
- Authentication (register, login)
- Patients (CRUD)
- Doctors (CRUD)
- Mappings (assign, list, delete)

Set the `baseUrl` variable to your server URL (default: http://localhost:8000).
The login request auto-captures the access token for use in other endpoints.
