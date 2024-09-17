num=input("Enter Number: ")
tup=("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine")
z=0
lst=list(num)
for j in lst:
        lst[z]=int(j)
        z+=1
for p in lst:
    print(tup[p],end=" ")
