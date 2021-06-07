FROM python:3.8-alpine
MAINTAINER Maksim wardomenmax@gmail.com
LABEL Weather_delivery

WORKDIR /python/src/getweather
COPY . .

RUN apk add --no-cache python3-dev \
                       build-base \
                       libc6-compat \
                       libffi-dev \
                       zlib-dev \
                       jpeg-dev \
                       linux-headers
RUN pip3 install --upgrade pip && apt-get clean
RUN pip3 install requests

EXPOSE 80

CMD [ "python3", "./weather_delivery.py" ]
