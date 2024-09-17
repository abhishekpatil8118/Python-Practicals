class MyException(Exception):
    def __init__(self,info):
        self.info=info
try:
    user=input("Enter username: ")
    pas=input("Enter password: ")
    if ((user=="abhi@gmail.com") and (pas=="Abhi@123")):
        pass
    else:
        raise MyException("Invalid username and password!")
except MyException as me:
    print("Error: ",me.info)
else:
    print("Login successful!")
