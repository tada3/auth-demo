# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir flask

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
