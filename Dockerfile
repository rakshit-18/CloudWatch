#Using the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the file to the working directory
COPY requirements.txt .

# Install the req. PY packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the app code to the working directory
COPY . .

# Set the Environment variable for the flask app
ENV FLASK_RUN_HOST=0.0.0.0

#Expose the port on which the flask app will run
EXPOSE 5000

# Start the flask app when the container runs
CMD [ "flask", "run" ]