str1 = raw_input("Enter a string to be analysed for frequency analysis: ")
str1 = str1.replace(' ','')
list1 = list(str1)
list2 = []
list3 = []
for i in xrange(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
        list3.append(1)
    else:
        for j in xrange(len(list2)):
            if list1[i] == list1[j] and i!=j:
                list3[j] += 1
for i in range(len(list2)):
    print "Frequency of the alphabet", list2[i], "is", list3[i]


