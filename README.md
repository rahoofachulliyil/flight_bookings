# Flight Booking System

This is a Django-based Flight Booking System API that allows users to search for flights, book tickets, and manage their bookings. Admin users can create and manage flights.

## Prerequisites

- Python 3.8+
- pip or Poetry
- PostgreSQL (if not using Docker)
- Docker (optional)

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/rahoofachulliyil/flight_bookings.git
   cd flight_booking
   ```

2. Set up the environment:

   If using pip:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   If using Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   poetry install
   poetry shell
   ```

3. Set up the database:

   Option 1: Using Docker (recommended)

   ```
   docker compose up -d db
   ```

   Option 2: Using local PostgreSQL installation

   - Install PostgreSQL if not already installed
   - Create a database using the credentials specified in the `.env` file

4. Set up environment variables:

   Create a `.env` file in the root directory with the following content:

   ```
   DEBUG="True"
   DATABASE_NAME="flight"
   DATABASE_USER="flight"
   DATABASE_PASSWORD="flight"
   DATABASE_HOST="localhost"
   ALLOWED_HOSTS="*"
   DATABASE_PORT=5432
   ```

5. Run migrations:

   ```
   python manage.py migrate
   ```

6. Create a superuser to add flight:

   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

The API should now be accessible at `http://localhost:8000/api/`.

## API Endpoints

- `/api/token/`: Obtain JWT token pair
- `/api/token/refresh/`: Refresh JWT token
- `/api/flights/`: List and create flights (GET, POST)
- `/api/flights/<id>/`: Retrieve, update, and delete flights (GET, PUT, DELETE)
- `/api/flights/search/`: Search for flights (GET)
- `/api/tickets/`: List and create tickets (GET, POST)
- `/api/tickets/<id>/`: Retrieve, update, and delete tickets (GET, PUT, DELETE)
- `/api/tickets/my_bookings/`: List user's bookings (GET)
