from Crypto.Cipher import AES
from os import urandom
import random

""" Write a function to detect the block size. I have assumed it to be 16 bytes here"""

""" Assume the encryption function to be hidden """
def encryption(plaintext):
    key = urandom(16)
    mode = random.randint(1,2)
    if mode == 1:
        obj = AES.new(key, AES.MODE_ECB)
        ciphertext = obj.encrypt(plaintext)
        return ciphertext
    elif mode == 2:
        IV = urandom(16)
        obj = AES.new(key,AES.MODE_CBC, IV)
        ciphertext = obj.encrypt(plaintext)
        return ciphertext

""" Assume the padding function to be hidden """
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

def detectmode():
    str1 = "abcdefghijklmnopabcdefghijklmnop"
    str1 = padding(str1)
    ciphertext = encryption(str1).encode("hex")
    print ciphertext
    if ciphertext[:32] == ciphertext[32:64]:
        print "ECB mode used"
    else:
        print "CBC mode used"

detectmode()

