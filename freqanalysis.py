str1 = raw_input("Enter a string to be analysed for frequency analysis: ")
list1 = list(str1)
list2 = []
list3 = []
for i in list1:
    if i not in list2:
        list2.append(i)
        list3.append(1)
    else:
        for j in range(len(list2)):
            if i == list1[j]:
                list3[j] += 1
for i in range(len(list2)):
    print "Frequency of the alphabet", list2[i], "is", list3[i]


