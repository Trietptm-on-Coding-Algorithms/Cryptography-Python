def hammdist(str1,str2):
    if len(str1) == len(str2):
        # Converting the text to binary form
        str1 = list(str1)
        str2 = list(str2)
        for i in xrange(len(str1)):
            str1[i] = bin(ord(str1[i]))
            str2[i] = bin(ord(str2[i]))
            str1[i] = str1[i].replace("0b","")
            str2[i] = str2[i].replace("0b","")

        # Pre-adding the bits to each element to make the size equal to 8 bits
        for i in xrange(len(str1)):
            if len(str1[i]) < 8:
                bit = 8 - len(str1[i])
                str1[i] = "0"*bit + str1[i]
            if len(str2[i]) < 8:
                bit = 8 - len(str2[i])
                str2[i] = "0"*bit + str2[i]
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        cnt = 0
        for i in xrange(len(str1)):
            if str1[i] != str2[i]:
                cnt += 1
        print "The hamming distance is ",cnt
        return cnt
        
    else:
        exit()
        
#def mainattack(
    




fo = open("ciphertext.txt","r")
chars = 0
str1 = ""
for line in fo:
    str1 += line
fo.close()
list1 = []
str1 = str1.replace("\n","")
str1 = str1.decode("base64")
for i in xrange(2,41):
    block1 = str1[:i]
    block2 = str1[i:2*i]
    print "Hamming for key ",i,": ",
    list1.append(hammdist(block1,block2))
    
print list1





