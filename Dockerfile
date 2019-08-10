# This template relies on the Python 3 alpine Docker image below
FROM python:3-alpine
LABEL maintainer="imadmoussa1@gmail.com"
# Create the application folder
RUN mkdir -p /var/app
WORKDIR /var/app

# Copy the requirements will be using
COPY requirements.txt /var/app
# Install the libraries
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps libffi-dev gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

# Run the flask server
ENV FLASK_APP=main.py
CMD flask run -h 0.0.0.0 -p 5000
