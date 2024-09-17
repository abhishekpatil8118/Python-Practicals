tup=(3,12,56,88,12,3)
print("repeated Items are ",end="")
for i in range(0,len(tup)):
    for j in range(i+1,len(tup)):
        if tup[i]==tup[j]:
            print(tup[i],end=" ")
