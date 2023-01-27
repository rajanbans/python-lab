#Ques3
l1=int(input("Enter first side of triangle="))
l2=int(input("Enter second side of triangle="))
l3=int(input("Enter third side of triangle="))
import math
if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    s=(l1+l2+l3)/2
    ar=math.sqrt(s*(s-l1)*(s-l2)*(s-l3))
    print("the area is=",ar)
else:
    print("the condition is invaid ")