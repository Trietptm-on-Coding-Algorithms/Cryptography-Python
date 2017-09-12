ct = raw_input("Enter ciphertext: ")           

list1 = [ct[i]+ct[i+1] for i in range(0,len(ct),2)]
for i in range(255):
    pt = ""
    for j in range(len(list1)):
        pt += hex(int(list1[j],16) ^ i)[2:].zfill(2)
    print pt.decode("hex")
    