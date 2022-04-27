##class my_class(object):
##    def __init__(self):
##        print('hello')
##
##    def fun(self):
##        print('welcome to friday')
##
##    def __new__(self):
##        print('my favorite day')
##
##my = my_class()
##my.fun()
##my.new()


##class my_class:
##    def __init__(self,name,age):
##
##        self.name = name
##        self.age = age
##
##    def one(self):
##        print('one',self.name)
##
##class second_class(my_class):
##    def two(self):
##        print('two',self.name,self.age)
##
##my = second_class('dhoni',33)
##my.one()
##my.two()

##class my_class:
##    def __init__(self,name,age,country):
##        self.name = name
##        self.age = age
##        self.country = country
##
##    def two(self):
##        print('one',self.name)
##
##class second_class(my_class):
##    def two(self):
##        print('two',self.name,self.age)
##
##class third_class(my_class):
##    def third(self):
##        print('third',self.name,self.name,self.country)
##
##my = third_class('sagara','India',22)
##my.two()
##my.third()

##class A:
##    def fun(self):
##        print("A")
##        
##class B(A):
##    def fun(self):
##        print('B')
##
##class C(A):
##    def fun(self):
##        print('c')
##
##class D(C,B):
##    pass
##    def fun(self):
##        print('D')
##d = D()
##d.fun()
 


              








    
