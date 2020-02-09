import pwn as p
from Crypto.PublicKey import ECC
import json
from base64 import b64encode, b64decode
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import string
from hashlib import sha256

message = {"aeskey": "nwmHkXTN/EjnoO5IzhpNwE3nXEUMHsNWFI7dcHnpxIIiXCO+dLCjR6TfqYfbL9Z6a7SNCKbeTFBLnipXcRoN6o56urZMWwCioVTsV7PHrlCU42cKX+c/ShcVFrA5aOTTjaO9rxTMxB1PxJqYyxlpNaUpRFslzj9LKH+g8hVEuP9lVMm7q4aniyOUgPrAxyn044mbuxPu6Kh+JHSt5dkmnPZGNfUDKCwvMKeilb5ZkLaW/EaoXXsJLh/wUinMROIqmD2dkiWnk10633sJIu1lEOUsiykYXtJcd3o/B2dfTx2/85C2J6IsIp3+jJne76AYryAONPSxuh+M0h1xCzNeQg==", "message": "6VCnnSOU1DBImyhlqt7SoEjRtmBxjmABFVmXYhlKDyc+NBlnZ3Hpj4EkLwydPGpHiAvr4R0zTXSyUnMk5N6fi0/BFZE=", "nonce": "Cems9uHF6mk=", "signature": "uhLCnBvGfdC1fVkGUKQ8zNp/fOXNnFxNuDEc7CDGEYSxnuZMoGqbEqMLguJqDdvHFSHoUrq2R9/+mfk8LHndhw==", "eccpubkey": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEGww+NA3xHj4kCyztekLhmJVB62Hhq/oGDWwo4fxgZCgbODqD3vrMFFTGCWfO8ZyHtstuW+Yztpq94CnSNpJoug=="}

ecckey = ECC.generate(curve='P-256')
signer = DSS.new(ecckey, 'fips-186-3')
eccpubkey = ecckey.public_key().export_key(format="DER")

def get_receipt(message):
	r = p.remote("crypto1.ctf.nullcon.net", 5001) # change this to server
	r.recvuntil("Enter message in json format: ")
	r.sendline(json.dumps(message))
	r.recvuntil("Here is your read receipt:")
	r.recvline()
	ret = r.recvline().strip().decode()
	r.close()
	return ret

sol = ""
for i in range(1, len(b64decode(message["message"])) + 1):
	print(f"Finding {i}th char")
	m = b64decode(message["message"])[:i]
	h = SHA256.new(b64decode(message["aeskey"]) + b64decode(message["nonce"]) + m) 
	signature = signer.sign(h)
	message2 = {"aeskey": message["aeskey"], "message": b64encode(m).decode(), "nonce": message["nonce"],
		 "signature":b64encode(signature).decode(), "eccpubkey":b64encode(eccpubkey).decode()}
	hm = get_receipt(message2)
	for c in string.printable:
		if sha256((sol + c).encode()).hexdigest() == hm:
			sol = sol + c
			break
print(sol)