FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

# --no-cache-dir reduces the size of the image by not create the cache dir
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
