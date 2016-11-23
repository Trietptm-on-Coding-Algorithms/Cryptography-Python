p = input("Enter the divisor number one: ")
q = input("Enter the divisor number two: ")
a = input("Enter remainder number one: ")
b = input("Enter remainder number two: ")
print "Okay, so the equations are as follows: "
print "x=", a, "mod", p
print "x=", b, "mod", q
print " "
#We need to find the value of x using Chinese Remainder Theorem
for i in range(1,p*q):
    if (i%p == a) and (i%q == b):
        x = i
print "The value of x is : ",x

        
    
