"""
   1
  212 
 32123
4321234
 32123
  212 
   1
"""
n=int(input())
for i in range(1,n+1):
    print((n-i)*' ',end='')
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(1,i+1):
        if j==1:
            continue
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    print((n-i)*' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(1,i+1):
        if(j==1):
            continue
        print(j,end='')
    print()