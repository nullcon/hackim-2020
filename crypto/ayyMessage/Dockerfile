FROM python:3.7-alpine
LABEL Description="ayymessage" VERSION='1.0'

RUN apk update && apk add socat gcc g++ make openssl-dev python3-dev python-dev libffi-dev autoconf

WORKDIR /opt/ayymessage
RUN mkdir -p /opt/ayymessage
COPY server.py .
COPY rsakey.pem .

RUN pip install pycryptodome

EXPOSE 5001
CMD ["socat", "TCP-LISTEN:5001,reuseaddr,nodelay,fork", "EXEC:python /opt/ayymessage/server.py"]