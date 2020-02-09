#!/usr/bin/env python3
from Crypto.PublicKey import RSA, ECC
import json
from hashlib import sha256
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

with open('rsakey.pem','r') as f:
	rsakey = RSA.import_key(f.read())


rsacipher = PKCS1_OAEP.new(rsakey)

def verify_message(message):
	eccpubkey = ECC.import_key(message["eccpubkey"])
	h = SHA256.new(message["aeskey"] + message["nonce"] + message["message"])
	verifier = DSS.new(eccpubkey, 'fips-186-3')

	try:
		verifier.verify(h, message["signature"])
		return True
	except ValueError:
		return False


def decrypt_message(message):
	aeskey = rsacipher.decrypt(message["aeskey"])
	ctr = AES.new(aeskey, AES.MODE_CTR, nonce=message["nonce"])
	return ctr.decrypt(message["message"])

def main():
	message = input("Enter message in json format: ")
	message = json.loads(message)

	message["nonce"] = b64decode(message["nonce"])
	message["message"] = b64decode(message["message"])
	message["aeskey"] = b64decode(message["aeskey"])
	message["signature"] = b64decode(message["signature"])
	message["eccpubkey"] = b64decode(message["eccpubkey"])

	if not verify_message(message):
		print("this message has been tampered with")
		exit(0)

	m = decrypt_message(message)
	hm = sha256(m).hexdigest()
	print("Here is your read receipt:")
	print(hm)



if __name__ == '__main__':
	main()