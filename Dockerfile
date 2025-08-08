# Use Python 3.11 (not 3.13)
FROM python:3.11-slim

# Where our app lives inside the container
WORKDIR /app

# Make Python behave nicely in containers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Start the app
CMD ["python", "main.py"]
