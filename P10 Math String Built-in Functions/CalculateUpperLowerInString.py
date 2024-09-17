str=input("Enter String: ")
ucount=0
lcount=0
for i in str:
    if(i.isupper()):
        ucount=ucount+1
    if(i.islower()):
        lcount=lcount+1
print("Upercase=",ucount,"Lowercase=",lcount)
