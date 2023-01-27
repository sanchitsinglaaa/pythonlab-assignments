#1
a=input("enter your string:")
x=len(a)
reverse_string=""
i=0
while i<=x:
  reverse_string += a[-(i+1)+x:-i+x]
  i=i+1
print(reverse_string)
#2
a = int(input("enter your number:"))
x = int(input('enter your first number in range:'))
y = int(input('enter your last number in range:'))
for i in range(x,y):
  if i%a==0:
    print(i)
#3
a=float(input("enter your first side:"))
b=float(input("enter your second side:"))
c=float(input("enter your third side:"))
if a+b>c and b+c>a and a+c>b:
   s= (a+b+c)/2
   area =(s*(s-a)*(s-b)*(s-c))**0.5
   print(area)
else :
  print("triangle does not exist")
#4
n = 5
'''
for i in range(n):
    for j in range(i):
        print ('* ',end="")
    print("")

'''
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print("")
#5
n=int(input("the number of rows to be printed="))
count=0
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+count),end=" ")
        count+=1
    print("")
    #6
    n1 = int(input("enter first number of range="))
    n2 = int(input("enter second number of range="))
    n = n1
    count = 0
    while (n <= n2):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n)
                count += 1
            n += 1
#7
n1=1
n2=500
count=0
for i in range(n1,n2+1):
    if i%7==0 and i%11==0:
        print(i)
        count+=1
print("the total no. of numbers=",count)
#8
s=[]
for n in range(0,10):
    a=int(input("Enter the number="))
    s.append(a)
print(s)
print("the positive nos. are=")
for i in s:
    if i>=0:
        print(i)
print("the negative nos. are=")
for i in s:
    if i<0:
        print(i)
print("the even nos. are=")
for i in s:
    if i%2==0:
        print(i)
print("the odd nos. are=")
for i in s:
    if i%2!=0:
        print(i)
print("To count number of occurences")
p=0
for i in s:
           p= s.count(i)
           print(f"{i}occurs {p} times")
#9
def counter(a,i):
    n=0
    n=a.count(i)
    return n
a=[]
x=int(input("enter no. of words to be entered in list="))
for i in range(0,x):
    y=input("enter word=")
    a.append(y)
print(a)
for i in a:
  print(f"{i} occurs {counter(a,i)} times")
