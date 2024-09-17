'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
z=2
for i in range(6,0,-1):
    for j in range(i,0,-1):
        print(" ",end="")
    y=1
    while y<z:
        print("* ",end="")
        y=y+1
    print()
    z=z+1
