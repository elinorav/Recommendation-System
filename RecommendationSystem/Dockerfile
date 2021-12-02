FROM python:3

ADD main/python/Server/Main.py /

RUN pip install yake bs4 lxml

CMD [ "python", "./main.py" ]

# syntax=docker/dockerfile:1

# FROM python:3.8-slim-buster
#
# WORKDIR /app
#
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
#
# COPY . .
#
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]