num=int(input("Enter any number:"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("Number is not Prime.")
            break
    else:
        print("Number is Prime.")
else:
    print("Number is not Prime.")
