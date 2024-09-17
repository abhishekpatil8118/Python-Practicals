num1=int(input("Enter a number: "))
num=num1
reverse=0
while num != 0:
    digit=num%10
    reverse=reverse*10+digit
    num //= 10
if(num1==reverse):
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")
