import heapq
n, k = map(int, input().split())
cost = list(map(int, input().split()))
dp = [[0,[]] for i in range(n)]
h = []
for i in range(k):
    heapq.heappush(h,[cost[n-1-i],n-1-i,[n-1-i]])
for i in range(n-k-1,-1,-1):
    while h[0][1]>i+k:
        heapq.heappop(h)
    dp[i][0] = h[0][0] + cost[i]
    dp[i][1] = [i] + h[0][2]
    heapq.heappush(h,[dp[i][0],i,dp[i][1]])
result = ' '.join(map(str, sorted(dp[0][1])))
print(result)

