#DP
# fibo using rec
'''def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(7))'''            
# or this is know as memerois
'''def fib(n):
    if dp[n-1]!=-1:
        return dp[n-1]
    if n==0:
        return 0
    if n==1:
        return 1
    dp[n-1]=fib(n-1)+fib(n-2)
    return dp[n-1]
dp=[1,-1,-1,-1,-1,-1]
print(fib(6))
print(dp)'''
# or this is tablulation
'''dp=[1,1]
for i in range(2,7):
    dp.append(dp[i-1]+dp[i-2])
print(dp)''' 