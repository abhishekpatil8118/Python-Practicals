class MyException(Exception):
    def __init__(self,info):
        self.info=info
try:
    raise MyException("Abhishek")
except MyException as me:
    print("Received Error: ",me.info)
else:
    print("Else block")
