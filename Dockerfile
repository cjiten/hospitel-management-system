# Use Python official image
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
# EXPOSE 8000

# Default command (overridden in docker-compose)
# CMD ["gunicorn", "hospitel_management_system.wsgi:application", "--bind", "0.0.0.0:8000"]
