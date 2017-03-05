n = input("Enter the size of the block required: ")
str1 = raw_input("Enter the string to be padded: ")

l = len(str1)
padlen = n % l

padbyte = hex(padlen).strip('0x')
if(len(padbyte)%2!=0):
    padbyte = "0" + padbyte

hexstr = str1.encode("hex")
hexstr += padlen*padbyte

hexstr = hexstr.decode("hex")
print hexstr


