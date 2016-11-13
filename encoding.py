temp1 = raw_input("Enter a number in hex: ")
num1 = int(temp1,16)
print "num1: ",num1
temp2 = raw_input("Enter another number in hex: ")
num2 = int(temp2,16)
print "num2: ",num2
xored = hex(num1 ^ num2)
print xored

