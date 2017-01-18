# python
name=input("what is your name? ") 
print("your  name is " + name)
age=input("enter your age: ")
age=int(age) #integer eþitliði yazabilmek için
a=int(age)
if a<18:
    print("You are too young to enter here")
elif a>=18:
    print("welcome" + name)