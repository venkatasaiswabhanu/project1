# FROM python:3.8
# WORKDIR /app
# COPY . /app

# CMD ["python", "app.py"]
# Use a base image that includes Python and MySQL client
FROM python:3.8

# Install MySQL client
RUN apt-get update && apt-get install -y mysql-client

# Set working directory
WORKDIR /app

RUN pip install -r requirements.txt

# Copy your Python script and any other necessary files
COPY app.py .

# Command to run your Python script
CMD ["python", "app.py"]
