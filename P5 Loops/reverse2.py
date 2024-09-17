'''
num=input("Enter number: ")
rev=0
pow=0
for i in num:
    rev+=int(i)*(10**pow)
    pow+=1
print("Reverse is: ",rev)

num=input("Enter a number: ")[::-1]
print(num)'''

num=input("Enter number: ")
for i in num:
    print(i)
