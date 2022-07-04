print("Hello, world.")
n="Ivan."
print("Hi,", n)
n=input("What's your name?")
print("Hi,", n)
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=input("Enter operacion:")
r=None
if c=="+":
    r=a+b
elif c=="-":
    r=a-b
elif c=="*":
    r= a*b
elif c=="/":
    r=a/b
elif c=="**":
    r=a**b
elif c=="%":
    r=a%b
elif c=="//":
    r=a//b
else :
    print("Incorect enter")
if r is not None:
    print("Result:",r)