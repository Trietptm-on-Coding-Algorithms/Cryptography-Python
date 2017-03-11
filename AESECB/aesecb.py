from Crypto.Cipher import AES

# Opening the file and decoding from base64
fo = open("encryptedtext.txt","r")
ciphertext = ""
for line in fo:
    ciphertext += line
ciphertext = ciphertext.replace("\n","")
ciphertext = ciphertext.decode("base64")

# Decrypting AES_EBC_128bit
obj = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
message = obj.decrypt(ciphertext)
print message



