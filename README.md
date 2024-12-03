# Connect me

This project is an application that connects people with similar interests, using a MySQL database.

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8+
- pip (Python package manager)
- Docker and Docker Compose

## Installation

Follow these steps to set up the project on your local machine:

1. Set Up a Virtual Environment

- Install virtualenv if not already installed:

```bash
  pip install virtualenv
```
- Create a virtual environment:
```bash
  virtualenv venv
```
- Activate the virtual environment:
  - Windows 
    ```bash
      .\venv\Scripts\activate
    ```
  - Linux/Mac
    ```bash
    source venv/bin/activate
    ```
2.  Install Dependencies
- Install all required dependencies using the following command:
```bash
  pip install -r requirements.txt
```

## Database Setup with Docker

1.  Start the MySQL Container
- Run the following command to start the MySQL container:
```bash
  docker-compose up -d
```
2.  Verify the Container
- Ensure the container is running by checking its status:
```bash
  docker ps
```

## Database Migration

1. Create Migrations 
- Generate the database schema migrations:
```bash
  python manage.py makemigrations
```

2. Apply Migrations
- Apply the migrations to the database:
```bash
  python manage.py migrate
```

## Populate database with fake data

Run the following command to populate the database with sample data:
```bash
  python manage.py populate_db
```
