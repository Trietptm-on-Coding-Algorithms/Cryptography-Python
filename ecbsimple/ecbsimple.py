from Crypto.Cipher import AES
from os import urandom

key = urandom(16)

def padding()


def encryption(key, plaintext):
    obj = AES.new(key,AES.MODE_ECB)
    ciphertext = obj.encrypt(plaintext)
    return ciphertext


secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".encode("base64")

plaintext = raw_input()
plaintext += secretsss
ciphertext = encryption(key, plaintext)

print ciphertext








