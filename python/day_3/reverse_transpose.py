a=[[1,2,3],
[4,5,6],
[7,8,9]]
b=[[0,0,0],[0,0,0],[0,0,0]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        b[i][j]=a[j][i]
        # print(a[i][j])
print(b)
for i in range(0,3,1):
    for j in range(2,-1,-1):
        print(b[i][j],end=" ")
    print(end=" ")
print("/n")
for i in range(2,-1,-1):
    for j in range(0,3,1):
        print(b[i][j],end=" ")
    print(end=" ")
