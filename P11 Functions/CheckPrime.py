def fun(num):
    flag=False
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                flag=True
                break
    if flag:
        print(num," is not prime number.")
    else:
        print(num," is prime number.")
n=int(input("Enter a number: "))
fun(n)