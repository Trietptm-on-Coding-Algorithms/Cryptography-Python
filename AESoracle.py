"""
An ECB/CBC detection oracle

Now that you have ECB and CBC working:

Write a function to generate a random AES key; that's just 16 random bytes.

Write a function that encrypts data under an unknown key --- that is, a function that generates a random key
and encrypts under it.

The function should look like:
    encryption_oracle(your-input)
    => [MEANINGLESS JIBBER JABBER]

Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes
after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random
IVs each time for CBC). Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. You should end up with a piece of code that,
pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening.

"""

from Crypto import Random
import random
from Crypto.Cipher import AES

# Generating a random number
def genrand():
    rand = Random.new()
    key = rand.read(16)
    return key

# Adding the string with bytes at the beginning and at the end
def addstring(str1):
    # Generate the number of bytes to be added randomly to str1 such that 5 <= randcnt <= 10
    randcnt = random.randint(5, 10)
    obj2 = Random.new()
    randbyte = obj2.read(randcnt)
    str1 = randbyte + str1 + randbyte
    return str1

def padding(str1):
    l = len(str1)
    padlen = 0
    if 16 > l:
        padlen = n - l
    elif 16 < l:
        i = 2
        while i < 50000:
            temp = 16
            temp *= i
            if temp > l:
                padlen = temp - l
                break
            i += 1
    padbyte = hex(padlen).replace("0x","")
    if len(padbyte) % 2 != 0:
        padbyte = "0" + padbyte
    hexstr = str1.encode("hex")
    hexstr += padlen * padbyte
    hexstr = hexstr.decode("hex")
    return hexstr


def encrypt():
    case = random.randint(1,1000)
    mode = "ecb" if case % 2 == 0 else "cbc"
    str1 = raw_input("Enter the message string to be encrypted: ")
    str1 = addstring(str1)
    str1 = padding(str1)
    if mode == "ecb":
        key = genrand()
        obj = AES.new(key,AES.MODE_ECB)
        ciphertext = obj.encrypt(str1)
        print "ECB mode used"
        return ciphertext
    elif mode == "cbc":
        key = genrand()
        iv = Random.new().read(16)
        obj = AES.new(key,AES.MODE_CBC,iv)
        ciphertext = obj.encrypt(str1)
        print "CBC mode used"
        return ciphertext


cipher = encrypt()
print "Cipher Text: ",cipher
hexstr = cipher.encode("hex")
print "Hex form of Cipher Text: ",cipher.encode("hex")














