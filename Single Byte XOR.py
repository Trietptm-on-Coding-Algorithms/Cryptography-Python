str1 = raw_input("Enter hex string: ")
str1 = list(str1)
for i in xrange(len(str1)-1):
    if i % 2 != 0:
        str1[i] = str1[i] + " "
str1 = ''.join(str1)
str1 = str1.split(" ")
temp = str1

for j in xrange(1,257):
    fl = 0
    str1 = temp
    for i in xrange(len(str1)):
        str1[i] = hex(int(str1[i],16) ^ j)
        str1[i] = str1[i].replace("0x","")
    str1 = ''.join(str1)
    if(len(str1)%2!=0):
        str1 = "0"+str1
    str1 = str1.decode("hex")
    print str1
    
            


