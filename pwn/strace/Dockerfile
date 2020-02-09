FROM python:3.7-slim-buster
LABEL maintainer="sudhackar"

RUN apt-get update && apt-get -y install socat

RUN pip3 install requests
COPY ./dist/strace /
COPY ./dist/server.py /
COPY flag .

RUN chown root:root flag
RUN chmod 700 flag
RUN chmod +x strace

RUN adduser --disabled-password --gecos '' pwn 

EXPOSE 8000

CMD ["socat", "-T60", "-b524288", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:python3 server.py,pty,stderr"]
