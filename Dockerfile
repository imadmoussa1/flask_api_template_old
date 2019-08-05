# This template relies on the Python gRPC Docker image below
FROM python:3

RUN mkdir -p /var/app
WORKDIR /var/app

COPY requirements.txt /var/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /var/app

# Compile protobuf files
ENV FLASK_APP=main.py
CMD flask run -h 0.0.0.0 -p 5000
