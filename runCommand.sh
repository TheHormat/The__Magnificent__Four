#!/bin/bash

# Starting Redis
echo "Starting Redis server..."
brew services start redis

# starting Celery worker
echo "Starting Celery worker..."
gnome-terminal -- bash -c "source venv/bin/activate && celery -A core worker --loglevel=info"

# starting Celery beat
echo "Starting Celery beat..."
gnome-terminal -- bash -c "source venv/bin/activate && celery -A core beat --loglevel=info"

# starting Django server
echo "Starting Django server..."
source venv/bin/activate && python manage.py runserver