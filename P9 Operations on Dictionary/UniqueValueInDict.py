dict1={"V":"S001","V":"S002","VI":"S001","VI":"S005","VII":"S005","V":"S009","VIII":"S007"}
tup=list(dict1.values())
print("Uniques Values: ")
for i in tup:
    c=tup.count(i)
    if c<2:
        print(i,end=" ")