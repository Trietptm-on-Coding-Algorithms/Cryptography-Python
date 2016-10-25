import base64
str1 = raw_input("Enter the hex code you wish to encode into base64 format: ")
print str1.decode('hex').encode('base64')
