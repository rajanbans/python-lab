year=int(input("Enter the year="))
if year%100==0:
    if year%400==0:
        print("it is a leap year")
    else:
        print("it is a non-leap year")
elif year%4==0:
        print("it is a leap year")
else:
        print("it is a non-leap year")