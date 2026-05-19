# using official Python image as base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file from local machine to container
COPY requirements.txt .

# Install Python dependencies mentioned in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . .

# Inform Docker that the application will run on port 5000.
EXPOSE 5000

# Command to start the Flask application when container starts
CMD ["python", "app.py"]
