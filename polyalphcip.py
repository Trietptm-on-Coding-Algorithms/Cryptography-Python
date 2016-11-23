encstr = []
str1 = raw_input("Enter the string to be encrypted: ")
list1 = list(str1)
str2 = raw_input("Enter the key string: ")
str2 = str2.upper()
list2 = list(str2)
for i in range(len(list2)):
    list2[i] = 1 + abs(ord('A')-ord(list2[i]))
#print list2
for i in range(len(str1)):
    c = i % (len(list2))
    if (ord(list1[i])+list2[c])>122:
        newkey = list2[c] - (122 - ord(list1[i]))
        list1[i] = chr(97 + (newkey-1))
        encstr.append(list1[i])
    else:
        list1[i] = chr(ord(list1[i])+list2[c])
        encstr.append(list1[i])
encstr = ''.join(encstr)
print "The encoded string is: ",encstr
