#1
num = int(input('enter the number'))
if num % 2 == 0:
    print("It is a even number")
else:
    print("It is a odd number")
#2
num=int(input("Enter the number"))
if num >= 0:
    print('positive number')
elif num <= 0:
    print('Negative number')
else:
    print("Zero")
#3
a=10
b=17

if a>b:
    print('largest number',a)
else:
    print("largest number",b)

#4
a=12
b=19
c=22

if a>b and a<c:
    print('largest number',a)
elif b<c:
    print('largest number',b)
else:
    print("largest number",c)

#5
age=int(input("Enter the age"))
if age>=18:
    print("eligibility of voting")
else:
    print("Not eligibility of voting")

#6
year=int(input('Eenter the year'))
if(year % 4 == 0 and year % 100!=0)or (year % 400 == 0):
    print("leap year")
else:
    print('not leap year')

#7
marks= int(input("Enter the marks"))
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print('Grade c')
else:
    print("fail")
#8
num=int(input("Enter the number"))
if num % 7 == 0:
    print('divisible by 7')
else:
    print("not divisible by 7")

#9
a=30
b=50
op=input('Enter the number(+,-,*,/):')
if op=="+":
    print('Result',a+b)
elif op=="-":
    print('Result',a-b)
elif op=="*":
    print('Result',a*b)
elif op=="/":
    print('Result',a/b)
else:
    print("Invaid operater")

#10
password=input("Enter the password")
if len(password) >= 8:
    print('strong password')
else:
    print('weak password')
    
