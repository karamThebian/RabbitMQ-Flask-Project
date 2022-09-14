FROM python:3.9.5-slim

RUN mkdir -p /usr/src/app

RUN apt-get update && apt-get install -y  build-essential patchelf libsodium23

COPY Microservices/ExchangeMicroservice/requirements.txt /usr/src/app/

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt


COPY Microservices/ExchangeMicroservice/ /usr/src/app

EXPOSE 9047

ENTRYPOINT ["gunicorn" , "-b", "0.0.0.0:9047", "-t", "120", "wsgi:app"]


