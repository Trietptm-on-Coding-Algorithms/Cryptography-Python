num1 = raw_input("Enter the first number in hex form: ")
c1 = int(num1,16)
binum1 = bin(c1)
print "binum1: ",binum1

num2 = raw_input("Enter the second number in hex form: ")
c2 = int(num2,16)
binum2 = bin(c2)
print "binum2: ",binum2

str1 = str(binum1).strip('0b')
str2 = str(binum2).strip('0b')
str3 = " "
print "str1: ", str1
print "str2: ", str2

for i in range(len(str1)):
    if str1[i] == str2[i]:
        str3 += '0'
    else:
        str3 += '1'
i = int(str3)
print hex(i)




