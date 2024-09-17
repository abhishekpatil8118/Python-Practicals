first=int(input("Enter marks of 1st subject: "))
second=int(input("Enter marks of 2nd subject: "))
third=int(input("Enter marks of 3rd subject: "))
fourth=int(input("Enter marks of 4th subject: "))
five=int(input("Enter marks of 5th subject: "))
total=first+second+third+fourth+five
per=(total/500)*100

if(per>=75):
    print("You got ",per,"% with A Grade.")
elif(per>=60):
    print("You got ",per,"% with B Grade.")
elif(per>=35):
    print("You got ",per,"% with C Grade.")
else:
    print("You got ",per,"% with D Grade.")
