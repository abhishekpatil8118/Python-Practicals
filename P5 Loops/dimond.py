for i in range(3):
    for z in range(4-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print(" ")

for i in range(3):
    for z in range(i+1):
        print(" ",end="")
    for j in range(2*(4 -i-1)-1):
        print("*",end="")
    print("")
