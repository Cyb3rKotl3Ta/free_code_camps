# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install system dependencies (if needed) and upgrade pip
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

# Install dependencies inside the virtual environment
ENV PATH="/py/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Command to run the application using the full path to uvicorn from the virtual environment
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
