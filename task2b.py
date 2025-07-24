n, k = map(int, input().split())
cost = list(map(int, input().split()))
dp = [[float("inf"),[]] for i in range(n+1)]
#print(dp)
dp[0] = [0,[]]
for i in range(1,n+1):
    for j in range(max(0,(i-k)),i):
        if dp[j][0]+cost[j]<dp[i][0]:
            dp[i][0] = dp[j][0]+cost[j]
            dp[i][1] = dp[j][1]+[j]
result = ' '.join(map(str, dp[-1][1]))
print(result)