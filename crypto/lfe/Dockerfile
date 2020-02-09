FROM python:3.7-alpine
LABEL Description="lfe" VERSION='1.0'

RUN apk update && apk add socat gcc g++ make openssl-dev python3-dev python-dev libffi-dev autoconf

WORKDIR /opt/lfe
RUN mkdir -p /opt/lfe
COPY secret.py .
COPY lfe.py .

RUN pip install parse pycryptodome

EXPOSE 5000
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,nodelay,fork", "EXEC:python /opt/lfe/lfe.py"]