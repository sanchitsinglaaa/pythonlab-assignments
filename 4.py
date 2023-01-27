#1
m=int(input("enter your marks"))
if m<25:
     print("Grade is F")
elif 25<=m<45:
     print("Grade is E")
elif 45<=m<50:
     print("Grade is D")
elif 50<=m<60:
     print("Grade is C")
elif 60<=m<80:
     print("Grade is B")
else:
     print("Grade is A")
     #2
y = int(input("enter year"))
if (y % 400 == 0):
         print(y, "is leap year")
elif (y % 100 == 0):
         print(y, "is not a leap year")
elif (y % 4 == 0):
         print(y, "is a leap year")
else:
         print(y, "is not a leap")
#3
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
#4
n=0
while(n<200):
    if n%5==2:
        if n%6==3:
            if n%7==2:
               print("the number of candies=",n)
    n+=1
