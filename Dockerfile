FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install -r requirements.txt

CMD [ "python", "main.py"]

