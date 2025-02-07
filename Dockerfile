FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files to container
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=10000

# Expose port
EXPOSE 10000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]