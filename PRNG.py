# The following code is an example of a PRNG(Pseudo Random Number Generators)
str1 = raw_input("Enter the string to be encoded: ")
list1 = list(str1)
seed = input("Enter the seed value, preferably a number with high number of digits: ")
# Seed is any true random number chosen
list2 = []
# The loop is for generating a pseudo random number
for i in range(1,len(str1)+1):
    sqr = str(seed * seed)
    extract = int(sqr[4])
    list2.append(extract)
    seed *= seed
print "The key generated is: ", list2
# The loop is for encoding the string by shifting it
for i in range(len(str1)):
    if ord(list1[i]) + list2[i] > 122:
        newkey = list2[i] - (122 - ord(list[i]))
        c = chr(97 + (newkey - 1))
        list1[i] = c
    else:
        c = chr(ord(list1[i]) + list2[i])
        list1[i] = c
list1 = ''.join(list1)
print "The encoded string using a PRNG is: ", list1






