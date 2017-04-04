def validate(str1):
    i = len(str1) - 1
    padbyte = str1[i-1] + str1[i]
    print padbyte
    padlen = int(padbyte, 16)
    print padlen
    j = 0
    while padlen > 0:
        print str1[i-1-j] + str1[i-j]
        if (str1[i-1-j] + str1[i-j]) != padbyte:
            print "Invalid Padding"
            exit()
        j += 2
        padlen -= 1
    print "Valid Padding!"
str1 = raw_input("Enter the hex form of string to be checked for validation of padding: ")
validate(str1)


