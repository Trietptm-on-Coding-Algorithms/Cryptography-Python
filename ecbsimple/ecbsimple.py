from Crypto.Cipher import AES
from os import urandom

key = urandom(16)


def padding(string):
    l = len(string)
    blocksize = 16
    padlen = blocksize - (l % blocksize)
    padbyte = hex(padlen).replace("0x", "")
    if len(padbyte) != 2:
        padbyte = "0" + padbyte
    string = string.encode("hex") + padlen*padbyte
    string = string.decode("hex")
    return string


def encryption(key, plaintext):
    obj = AES.new(key, AES.MODE_ECB)
    cipher = obj.encrypt(plaintext)
    return cipher.encode("hex")

secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
secret = secret.decode("base64")

revealed = ""
for k in xrange(len(secret)/16):
    b = ""
    for i in xrange(1,17):
        prepend = "a"*(16-i)
        plaintext = prepend + secret[0+k*16:]
        plaintext = padding(plaintext)
        ciphertext = encryption(key, plaintext)
        for j in xrange(256):
            check = prepend + b + chr(j)
            encrypted = encryption(key, check)
            if encrypted == ciphertext[:32]:
                b += chr(j)
                break
    revealed += b
print revealed


