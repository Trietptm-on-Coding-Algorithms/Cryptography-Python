n = input("Enter the size of the block required: ")
str1 = raw_input("Enter the string to be padded: ")
print "The encoded form of the original string without padding: ",str1.encode("hex")
l = len(str1)
print "Length of the string given as input: ",l

if n>l:
    padlen = n - l
elif n<l:
    i=2;
    while i<50000:
        temp = n
        temp *= i
        if temp > l:
            padlen = temp - l
            break
        i += 1
else:
    padlen = n

print padlen
padbyte = hex(padlen).replace("0x","")
print "The byte to be padded at the end of the string: ",padbyte

print "padbyte: ",padbyte
if(len(padbyte)%2!=0):
    padbyte = "0" + padbyte

str1 = str1.encode("hex")
str1 += padlen*padbyte
print "The hex form of the string is: ", str1
print str1
print len(str1)



print "The hex decoded, padded hex string: ",str1.decode("hex")



