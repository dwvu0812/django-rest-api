# AirCnC Clone - Django REST API

A modern Airbnb clone built with Django REST Framework, following industry best practices.

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd aircnc-clone
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate      # Linux/Mac
   ```

3. **Install dependencies**

   ```bash
   # Core dependencies
   pip install -e .

   # Development dependencies
   pip install -e ".[dev]"

   # All dependencies (dev + test + docs)
   pip install -e ".[all]"
   ```

4. **Set up environment variables**

   ```bash
   cp env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 📦 Dependency Management

This project uses `pyproject.toml` for modern Python dependency management:

- **Core dependencies**: Automatically installed with `pip install -e .`
- **Development tools**: `pip install -e ".[dev]"` (black, flake8, isort, etc.)
- **Testing tools**: `pip install -e ".[test]"` (pytest, coverage, etc.)
- **Documentation**: `pip install -e ".[docs]"` (mkdocs, etc.)
- **Production**: `pip install -e ".[prod]"` (gunicorn, sentry, etc.)

## 🛠️ Development Tools

- **Code formatting**: `black .`
- **Linting**: `flake8`
- **Import sorting**: `isort .`
- **Type checking**: `mypy` (when added)
- **Pre-commit hooks**: `pre-commit install`

## 📁 Project Structure

```
aircnc_clone/
├── config/                 # Django settings
│   ├── settings/
│   │   ├── base.py        # Common settings
│   │   ├── local.py       # Development
│   │   └── production.py  # Production
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                   # Django applications
│   ├── users/             # User management
│   ├── properties/        # Property listings
│   ├── bookings/          # Reservation system
│   ├── reviews/           # Rating system
│   ├── messaging/         # Real-time chat
│   └── notifications/     # Push notifications
├── core/                   # Shared utilities
├── static/                 # Static files
├── media/                  # User uploads
├── tests/                  # Test files
└── pyproject.toml         # Dependencies & config
```

## 🎯 Learning Approach

This project follows a structured learning methodology:

1. **Analyze** - Understand requirements and best practices
2. **Design** - Plan architecture and implementation
3. **Implement** - Build features step by step
4. **Reflect** - Review and improve

## 📚 Technology Stack

- **Backend**: Django 3.2, Django REST Framework
- **Database**: PostgreSQL (production), SQLite (development)
- **Caching**: Redis
- **Task Queue**: Celery
- **Authentication**: JWT + OAuth (Google, Facebook)
- **API Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Code Quality**: Black, Flake8, isort, pre-commit
