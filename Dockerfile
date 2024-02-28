# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install flask

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Run app.py when the container launches
CMD ["python", "app.py"]