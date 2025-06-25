FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libgtk2.0-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY face_blur.py .
COPY models/ /app/models/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Entry point
ENTRYPOINT ["python", "face_blur.py"]

