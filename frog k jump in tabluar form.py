# frog k jump in tabluar form
a=[10,20,30,10]
dp=[99999]*len(a)
dp[1]=abs(a[0]-a[1])
k=3
for i in range(1,len(a)):
    for j in range(1,k+1):
        d=dp[i-j]+abs(a[i]-a[i-j])
        dp[i]=min(d,dp[i])
print(dp[len(a)-1])