FROM python:3.7-alpine
LABEL Description="rps" VERSION='1.0'

RUN apk update && apk add socat gcc g++ make openssl-dev python3-dev python-dev libffi-dev autoconf

WORKDIR /opt/rps
RUN mkdir -p /opt/rps
COPY secret.py .
COPY rps.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,nodelay,fork", "EXEC:python /opt/rps/rps.py"]