#1
a="Hello World"
reverse_name=a[::-1]
print(reverse_name)

#2
a='madam'
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#3
c=str(input("enter a word="))
d=''
for i in c:
    if i not in d:
        d=d+i
        print(c.count(i))
#4
a="progamin"
b=""
for i in a:    
    if i not in b:
        b=b+i
print(b)

#5
a="aabbcddee"
for c in a:
    if a.count(c)==1:
        print(c)
        
#6
a="Python is easy"


    






