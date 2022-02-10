def countercloskwise(mat ,r ,c):
    r,c=r-1,c-1
    t,l=0,0
    ans=[]
    d=0
    while t<=r and l<=c:
        if d==0:
            for i in range(t,r+1):
                ans.append(mat[i][l])
            l+=1
        if d==1:
            for i in range(l,c+1):
                ans.append(mat[r][i])
            r-=1
        if d==2:
            for i in range(r,t-1,-1):
                ans.append(mat[i][c])
            c-=1
        if d==3:
            for i in range(c,l-1,-1):
                ans.append(mat[t][i])
            t+=1
        d=(d+1)%4
    return ans






r=int(input())
mat=[]
for i in range(r):
    ans=list(map(int,input().split(" ")))
    mat.append(ans)
print(mat)
print("Counter clockwisse spiral traversal=>")
p=countercloskwise(mat,3,3)
for i in p:
    print(i,end=" ")