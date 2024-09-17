year=int(input("Enter year: "))
if(year%4==0):
    print(year," is Leap year.")
elif(year%400==0):
    print(year," is Leap year.")
elif(year%100==0):
    print(year," is not a leap year.")
else:
    print(year," is not a leap year.")
