a=[(1,2),(2,5),(4,6),(6,7),(5,8),(7,9)]
d=[5,6,5,4,11,2]
dp=d.copy()
for j in range(1,len(d)):
    for i in range(0,j):
        if a[i][1]<=a[j][0]:
            dp[j]=max(d[j]+dp[i],dp[j])
print(dp)
print(dp[i])