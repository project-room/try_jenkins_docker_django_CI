FROM python:3.5-slim

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y vim wget curl net-tools libmysql++-dev gcc && \
    pip3 install django==1.11 mysqlclient

RUN mkdir -p /var/www/project/app/backend && \
    mkdir -p /var/www/project/app/frontend && \
    mkdir -p /var/www/project/app/static && \
    mkdir -p /var/www/project/logs && \
    mkdir -p /var/www/project/configs && \
    mkdir -p /var/www/project/fixtures

USER root

WORKDIR /var/www/project/

CMD ["python3"]
