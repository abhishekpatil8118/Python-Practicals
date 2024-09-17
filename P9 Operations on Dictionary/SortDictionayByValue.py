dict1={"Three":3,"One":1,"Four":4,"Two":2}
lst=sorted(dict1.values(),reverse=True)
sorted_dict={}

for i in lst:
    for j in dict1.keys():
        if dict1[j]==i:
            sorted_dict[j]=dict1[j]
            break
print(sorted_dict)
