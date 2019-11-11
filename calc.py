def add(a, b):
   return a+b

def sub(a, b):
   return a-b

def mul(a, b):
   return a*b

def div(a, b):
    return a/b

print("Select an operation:")
print("+")
print("-")
print("*")
print("/")

choice = input("Enter operator to use:")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if choice == '+':
   print(x,"+",y,"=", add(x,y))
elif choice == '-':
   print(x,"-",y,"=", sub(x,y))
elif choice == '*':
   print(x,"*",y,"=", mul(x,y))
elif choice == '/':
   print(x,"/",y,"=", div(x,y))
else:
    print("Invalid input")