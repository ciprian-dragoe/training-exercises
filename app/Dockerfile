FROM python:3.8-slim-buster
COPY ./app/ /app/
WORKDIR /app
RUN apt-get clean
RUN apt-get -y update
RUN apt-get upgrade -y
RUN apt-get -y install nginx
RUN apt-get install -y python3
RUN apt-get -y install python3-dev
RUN apt-get -y install build-essential
RUN apt-get -y install curl
COPY ./app/nginx.conf /etc/nginx

ENV DOCKERVERSION=20.10.13
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz && tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 -C /usr/local/bin docker/docker && rm docker-${DOCKERVERSION}.tgz

RUN curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

RUN pip install -r /app/requirements.txt
RUN chmod +x /app/start_server.sh
CMD ["/app/start_server.sh"]
