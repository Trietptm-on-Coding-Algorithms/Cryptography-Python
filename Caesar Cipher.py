import sys

s = raw_input().strip()
k = int(raw_input().strip())  
k=k%26
encstr = []
decstr = list(s)
for i in decstr:
    if ord(i)>=97 and ord(i)<=122:
        if (ord(i)+k)>122:
            newkey = k - (122 - ord(i))
            i = chr(97 + (newkey-1))
            encstr.append(i)
        else:
            i = chr(ord(i)+k)
            encstr.append(i)
    elif ord(i)>=65 and ord(i)<=90:
        if (ord(i)+k)>90:
            newkey = k - (90 - ord(i))
            i = chr(65 + (newkey-1))
            encstr.append(i)
        else:
            i = chr(ord(i)+k)
            encstr.append(i)
    else:
        encstr.append(i)
        
encstr = ''.join(encstr)
print encstr