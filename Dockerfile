FROM python:3.10.12

MAINTAINER Tan Jin (tjtanjin)

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .
RUN mkdir ./images

# install app-specific dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-telegram-bot[job-queue]

# app command
CMD ["python", "-u", "./main.py"]