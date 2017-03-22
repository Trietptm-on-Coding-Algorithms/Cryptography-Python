n = input("Enter the size of the block required: ")
str1 = raw_input("Enter the string to be padded: ")
print "The encoded form of the original string without padding: ",str1.encode("hex")
l = len(str1)
print "Length of the string given as input: ",l

padlen = n - ( l % n)

padbyte = hex(padlen).replace("0x","")
if(len(padbyte)%2!=0):
    padbyte = "0" + padbyte
print "The byte to be padded at the end of the string: ",padbyte

str1 = str1.encode("hex")
str1 += padlen*padbyte
print "The hex form of the padded string is: ", str1






