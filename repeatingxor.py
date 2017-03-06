str1 = raw_input("Enter the string to be encrypted: ")
str1 = str1.encode("hex")
str1 = str1.replace(" ","")

#Splitting the hex string per byte
str1 = list(str1)
for i in xrange(len(str1)):
    if i%2 != 0:
        str1[i] += " "
#print str1
str1 = ''.join(str1)
str1 = str1.split(" ")
#print str1
del str1[len(str1)-1]
#print str1


key = ['I','C','E']
keylen = len(key)
for i in xrange(len(str1)):
    mod = i % keylen
    str1[i] = hex(int(str1[i],16) ^ ord(key[mod]))
print str1

for i in xrange(len(str1)):
    str1[i] = str1[i].replace("0x","")
    if(len(str1[i])%2 != 0):
        str1[i] = "0" + str1[i]
str1 = ''.join(str1)

print str1


        
        

    
