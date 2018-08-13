FROM python:3.5-alpine

RUN echo "更换 Debian 源为中科大源" && \
    sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \    
    echo "更新 apt 源" && \
    apt-get update

CMD ["python3"]
