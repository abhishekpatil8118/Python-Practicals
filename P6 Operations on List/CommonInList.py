lst1=[4,6,3,9,12,15]
lst2=[6,2,1,25,7,9]
lst3=[]
for i in lst1:
    for j in lst2:
        if i==j:
            lst3.append(j)
print("Common elements: ",lst3)
