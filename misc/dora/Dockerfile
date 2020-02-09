FROM python:2.7-alpine

EXPOSE 8000

RUN apk --no-cache add socat

COPY server.py /home
COPY b64 .

RUN chmod +x /home/server.py
RUN chmod 777 /home/server.py

CMD ["socat", "TCP4-LISTEN:8000,fork,reuseaddr", "EXEC:\"python -u /home/server.py\""]
