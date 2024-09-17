def cal(str1):
    ucount=0
    lcount=0
    for i in str1:
        if i.isupper():
            ucount=ucount+1
        if i.islower():
            lcount=lcount+1
    print("Uppercase: ",ucount,"Lowercase: ",lcount)
str1=input("Enter a String: ")
cal(str1)
