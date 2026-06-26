class demo:
    def fun(sef):
        print("I am in demo class")
obj=demo()
obj.fun()

#self current obj
name="Alice"
grade="A"
def display_info(self):
    print(f"student Name:(self_name),Grade:({self, grade}")

#Mulity
class Grandparent:
    def fuction(self):
        print("Grandparent")

obj=Grandparent()
obj.fuction()

class parent:
    def fun1(self):
        print('parent')
        
obj=parent()
obj.fun1()


class father:
    def fa(self):
        print("father")

class mother:
    def mo(self):
        print('mother')

class child(father,mother):
    def ch(self):
        print('child')

obj=child()
obj.fa()
obj.mo()
obj.ch()


