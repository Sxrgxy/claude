# Start with Python 3.12
FROM python:3.12-slim

# Set up your working directory
WORKDIR /app

# Copy just the requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your code
COPY . .

# Tell Docker what to run when we start our container
CMD ["python", "src/main.py"]