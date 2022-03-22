FROM python:3.8-slim-buster
COPY ./app/ /app/
WORKDIR /app
RUN apt-get clean && apt-get -y update && apt-get -y install nginx && apt-get -y install python3-dev && apt-get -y install build-essential
RUN pip install -r /app/requirements.txt
COPY ./app/nginx.conf /etc/nginx
RUN chmod +x /app/start_prod_server.sh
CMD ["/app/start_prod_server.sh"]
