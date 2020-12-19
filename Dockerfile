# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

#RUN chmod 777 -R ~/Desktop/covidapp

# Install dependencies
RUN pip install -r /code/requirements.txt



