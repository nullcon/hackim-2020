FROM ubuntu:18.04
MAINTAINER unknonwn
LABEL Description="year-3000" VERSION='1.0'

#installation
RUN apt-get update
RUN apt-get install -y socat
RUN apt-get install -y python3
RUN apt-get install -y gcc-multilib

#user
RUN adduser --disabled-password --gecos '' re
RUN chown -R root:re /home/re/
RUN chmod 750 /home/re

RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

#Copying file
WORKDIR /home/re/
COPY dist/year3000.tar.gz /home/re
COPY deploy.py /home/re

#Setting perm.
RUN chown root:re /home/re/year3000.tar.gz
RUN chown root:re /home/re/deploy.py
WORKDIR /home/re
RUN tar xzf year3000.tar.gz
RUN chown root:re *.bin
RUN chmod +x *.bin

#Run the program with socat
CMD su re -c "socat TCP-LISTEN:1234,reuseaddr,fork EXEC:\"python3 deploy.py\""
