#!/usr/bin/python3
import os
import stat
import subprocess
import uuid

import requests

url = input("Send your js")

r = requests.get(url, stream=True)

tmpfile_path = "/tmp/" + str(uuid.uuid4()) + ".js"

with open(tmpfile_path, "wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

st = os.stat(tmpfile_path)
os.chmod(tmpfile_path, 0o777)

subprocess.run(
    [
        "/js",
        tmpfile_path])

# os.remove(tmpfile_path)