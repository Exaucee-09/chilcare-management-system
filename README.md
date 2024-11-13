# Childcare Management System

## Overview
This is a Django-based childcare management system that allows administrators to manage records for children and staff with full CRUD (Create, Read, Update, Delete) functionality.

## Features
- **Children App**: Add, edit, view, and delete child profiles.
- **Staff App**: Add, edit, view, and delete staff member profiles.
- Admin and guest user authentication.
- Easy navigation via a dashboard (planned for the project).

## Installation and Setup

### Prerequisites
- Python 3.x
- Django 4.x (or compatible version)
- Git
- Virtual environment tool (optional but recommended)

### Steps to Clone and Run the Project Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/childcare-management-system.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd childcare-management-system
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

4. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the app**:
    - Visit `http://127.0.0.1:8000/` in your web browser.
    - Log in with your admin credentials to manage children and staff records.

## Future Enhancements
- Add profiles for children and staff with photos.
- Extend the dashboard to integrate new apps and provide more comprehensive data visualization.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)

