# Use official Python 3.11.13 image
FROM python:3.11.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Run your CLI app
CMD ["python", "app.py"]
