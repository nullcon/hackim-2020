#!/usr/bin/python3
import os
import stat
import subprocess
import uuid

import requests

url = input("Where are you from?")

r = requests.get(url, stream=True)

tmpfile_path = "/tmp/" + str(uuid.uuid4())

with open(tmpfile_path, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

st = os.stat(tmpfile_path)
os.chmod(tmpfile_path, 0o777)

subprocess.run(
    [
        "/strace",
        "-e",
        "fault=execve,execveat,clone,clone3,setns,unshare,fork,getuid,setfsuid,setuid,setgid,getresuid,setreuid,setresuid,chown,fchown,setgroups,setgroups,ptrace",
        "-u",
        "pwn",
        tmpfile_path])

os.remove(tmpfile_path)