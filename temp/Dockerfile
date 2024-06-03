#for testi
FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

COPY niggasan.sh .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash", "niggasan.sh"]
