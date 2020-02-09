from Crypto.PublicKey import RSA, ECC
import json
from hashlib import sha256
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64encode
import os
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

m = input("Message: ").encode()

with open('rsapubkey.pem','r') as f:
	rsakey = RSA.import_key(f.read())
rsacipher = PKCS1_OAEP.new(rsakey)

ecckey = ECC.generate(curve='P-256')

signer = DSS.new(ecckey, 'fips-186-3')
aeskey = os.urandom(16)
aescipher = AES.new(aeskey, AES.MODE_CTR)
c = aescipher.encrypt(m)
aeskeyenc = rsacipher.encrypt(aeskey)

h = SHA256.new(aeskeyenc + aescipher.nonce + c) 
signature = signer.sign(h)
eccpubkey = ecckey.public_key().export_key(format="DER")

message = {"aeskey": b64encode(aeskeyenc).decode(), "message": b64encode(c).decode(), "nonce": b64encode(aescipher.nonce).decode(),
	 "signature":b64encode(signature).decode(), "eccpubkey":b64encode(eccpubkey).decode()}
message = json.dumps(message)
print(message)