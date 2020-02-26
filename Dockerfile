# set official base image
FROM python:3.8.1-alpine

# set the workdirectory
WORKDIR /app

# set the environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# set the dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy the project
COPY . .

# set the project to the user
RUN adduser -D raselrostock
USER raselrostock

# run gunicorn
CMD gunicorn djnunu.wsgi:application --bind 0.0.0.0:$PORT

