class alpha:
    def fun(self,i,c):
        print("Integer: ",i,"Character: ",c)
    def fun(self,c,i):
        print("Character: ",c,"Integer: ",i)
obj1=alpha()
obj1.fun(2245,"A")
obj1.fun("A",2245)
