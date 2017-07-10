from os import urandom

plain_list = []
cipher_list = []
plaintext = raw_input()
plain_list = list(plaintext)

print plain_list

key = urandom(1)

print "The key is: ",key.encode("hex")
for i in xrange(len(plain_list)):
    xored = chr(ord(plain_list[i]) ^ ord(key))
    cipher_list.append(xored.encode("hex"))
ciphertext = ''.join(cipher_list)
print ciphertext


