try:
    a=int(input("Enter a "))
    b=int(input("Enter b "))
    c=a/b
    print("a/b=",c)
except Exception:
    print("can't divide by zero")