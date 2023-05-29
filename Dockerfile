# Use the official Python base image
FROM python:3.10.6

# Set the working directory in the container
WORKDIR /django_network_inventory

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN python -m pip install -r requirements.txt

# Copy the Django project code to the working directory
COPY . .

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000
