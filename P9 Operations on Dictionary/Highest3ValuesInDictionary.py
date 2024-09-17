dict1={"Two":2,"Ten":10,"Fifty":50,"Thirty":30,"Five":5,"Fourty-Five":45}
lst=list(dict1.values())
lst.sort(reverse=True)
print("Highest values are: ",end="")
for i in range(0,3):
    print(lst[i],end=" ")
