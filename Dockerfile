FROM python:3.12-slim

WORKDIR /app

# Install required system libs for PaddleOCR & OpenCV-lite backend
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python deps
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app
COPY app/ ./app

EXPOSE 8080

# API key
ENV VALID_API_KEY=my-secret-api-key

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
