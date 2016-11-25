import random
str1 = raw_input("Enter the string to be encoded: ")
list1 = list(str1)
list2 = []
for i in range(len(str1)):
    c = random.randint(1,25)
    list2.append(c)
print list2
for i in range(len(str1)):
    if ord(list1[i]) + list2[i] > 122:
        newkey = list2[i] - (122 - ord(list1[i]))
        c = chr(97 + (newkey-1))
        list1[i] = c
    else:
        c = chr(ord(list1[i]) + list2[i])
        list1[i] = c
list1 = ''.join(list1)
print "The encoded string is: ",list1



