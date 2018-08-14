FROM python:3.5-slim

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y vim wget curl net-tools libmysql++-dev gcc && \
    pip3 install django==1.11 mysqlclient

CMD ["python3"]
