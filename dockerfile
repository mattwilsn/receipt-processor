FROM python:3.11-slim

# Create a non-root user to run the application
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set up the working directory with proper permissions
WORKDIR /app

# Copy requirements file and install dependencies as root
COPY requirements.txt .
RUN pip3 install --no-cache-dir --progress-bar off -r requirements.txt

# Copy application code
COPY . .

# Set proper ownership of the application directory
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
