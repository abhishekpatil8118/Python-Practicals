for i in range(3):
    for z in range(i+1):
        print(" ",end="")
    for j in range(2*(4-i-1)-1):
        print("1",end="")
        print("01",end="")
    print("")
