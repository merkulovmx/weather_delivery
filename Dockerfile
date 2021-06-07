FROM python:3.8-alpine
MAINTAINER Maksim wardomenmax@gmail.com

WORKDIR /python/src/getweather
COPY . .

RUN apk add --no-cache python3-dev \
                       build-base \
                       libc6-compat \
                       libffi-dev \
                       zlib-dev \
                       jpeg-dev \
                       linux-headers
RUN pip3 install --upgrade pip
RUN pip install requests

EXPOSE 80

ENTRYPOINT [ "python3", "./weather_delivery.py"]
