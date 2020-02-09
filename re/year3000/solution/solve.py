import socket
import subprocess
import time
import re
import telnetlib

SERVER = ('localhost', 1234)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.connect(SERVER)

def run_s(name):
    out = subprocess.check_output(['python3', name])
    return out

while True:
    data = s.recv(1023)
    data = data.decode('utf-8')
    print(repr(data))
    data = re.search('\d+\.bin', data)
    data = data.group()
    data = data.strip('.bin')
    data = 'sol_' + data + '.py'
    ans = run_s(data)
    s.send(ans)
    time.sleep(0.3)
