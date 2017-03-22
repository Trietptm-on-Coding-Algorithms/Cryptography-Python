from Crypto.Cipher import AES
from os import urandom

key = "\xa7\xcc\xef\x03X\xc9\x9e\x108\xed\xe1\x8e \xb9\xc9\x0c"


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
secret = secret.decode("base64").replace("\n","").replace(" ","")

plaintext = raw_input()
plaintext += secret
print "length of the text to be encrypted: ",len(plaintext)
plaintext = padding(plaintext)
ciphertext = encryption(key, plaintext)
print "Length of ciphertext: ",len(ciphertext)
print "Size of ciphertext: ",len(ciphertext)/2
print ciphertext
temp = ciphertext

secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
secret = secret.decode("base64").replace("\n","").replace(" ","")[1:]


for i in xrange(0,255):
    plaintext = "aaaaaaaaaaaaaaaaaaa"
    plaintext += chr(i) + secret
#    print "length of the text to be encrypted: ",len(plaintext)
    plaintext = padding(plaintext)
    ciphertext = encryption(key, plaintext)
#print "Length of ciphertext: ",len(ciphertext)
#print "Size of ciphertext: ",len(ciphertext)/2
#print ciphertext
    if ciphertext == temp:
        print "Found First byte: ",chr(i)
        exit()
print "Wrong Algorithm"









