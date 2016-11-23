m = input("Enter the dividend m: ")
a = input("Enter the divisor a: ")
e = input("Enter the exponent e: ")
print "Umm, so you want to solve the following equation: a^e mod m"
mod = 1
for i in range(1,e+1):
    mod = (mod*a) % m
print mod

    
