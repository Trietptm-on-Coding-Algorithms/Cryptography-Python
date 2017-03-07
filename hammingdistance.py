# Input the strings
str1 = raw_input("Enter string number 1: ")
str2 = raw_input("Enter string number 2: ")

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
        print str1
        print str2
        cnt = 0
        for i in xrange(len(str1)):
            if str1[i] != str2[i]:
                cnt += 1
        print "The hamming distance is ",cnt
        
else:
    exit()