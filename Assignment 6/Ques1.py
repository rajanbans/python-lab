n=int(input("Enter number to be checked= "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("The number is perfect")
else:
    print("The number is not  perfect")