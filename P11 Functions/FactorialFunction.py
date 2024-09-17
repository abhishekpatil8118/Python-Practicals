def fun1(num):
    if num<0:
        print("Enter positive number.")
    else:
        var=1
        for i in range(1,num+1):
            var=var*i
        print("factorial is ",var)
num=int(input("Enter a number: "))
fun1(num)
