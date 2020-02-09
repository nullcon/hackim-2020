FROM ubuntu:18.04
MAINTAINER unknonwn
LABEL Description="ch0c0l4te-chip" VERSION='1.0'

#installation
RUN apt-get update
RUN apt-get install -y socat

#user
RUN adduser --disabled-password --gecos '' pwn
RUN chown -R root:pwn /home/pwn/
RUN chmod 750 /home/pwn

RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

#Copying file
WORKDIR /home/pwn/
COPY dist/main /home/pwn
COPY src/ch0c0l4te-chip /home/pwn
COPY flag /home/pwn

#Setting perm.
RUN chown root:pwn /home/pwn/flag
RUN chmod +x /home/pwn/main
RUN chmod 440 /home/pwn/flag

#Run the program with socat
WORKDIR /home/pwn
CMD su pwn -c "socat TCP-LISTEN:1234,reuseaddr,fork EXEC:./main"
