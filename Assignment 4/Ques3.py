import random
n=1
while(n<11):
  n1=random.randint(1,10)
  n2=random.randint(1,10)
  r=n1*n2
  print("Question",n,":",n1,"*",n2)
  ans=int(input())
  if r==ans:
    print("Right!")
  else:
    print("wrong")
    print("correct answer is=",r)
  n+=1