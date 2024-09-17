num= int(input("Enter a Number: "))
Sum=0
while num>0:    
    Sum += num %10       
    num = num//10    
print("Sum of digits of given no. is :" ,Sum)
