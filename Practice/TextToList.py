num=input("Enter a number: ")
lst=list(num)
lst.reverse()
temp=lst
num1=""
for i in temp:
    num1=num1+i
if num==num1:
    print("PALINDROME.")
else:
    print("NOT PALINDROME.")
