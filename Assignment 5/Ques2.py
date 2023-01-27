n1=int(input("enter the first number of the range="))
n2=int(input("enter the second number of the range="))
n3=int(input("enter number for which multiples have to be found="))
count=0
n=n1
while n<=n2 :
   if n%n3==0:
     print(n)
     count+=1
   n+=1
print("total numbers=",count)
  

