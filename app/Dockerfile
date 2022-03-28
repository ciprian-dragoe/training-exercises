FROM python:3.8-slim-buster
COPY ./app/ /app/
WORKDIR /app
RUN apt-get clean && apt-get -y update && apt-get -y install nginx && apt-get -y install python3-dev && apt-get -y install build-essential && apt-get -y install curl
RUN pip install -r /app/requirements.txt
COPY ./app/nginx.conf /etc/nginx
ENV DOCKERVERSION=20.10.13
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
  && tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 -C /usr/local/bin docker/docker \
  && rm docker-${DOCKERVERSION}.tgz
COPY ./app/start_server.sh /app/start_server.sh
RUN chmod +x /app/start_server.sh
CMD ["chmod +x /app/start_server.sh && /app/start_server.sh"]
