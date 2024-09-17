num=input("Enter a number: ")
lst=list(num)
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end="")
