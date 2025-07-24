def min_cost_to_cross_river(n, cost, k, m):
    dp = [[float('inf')] * (m+1) for _ in range(n)]
    path = [[[] for _ in range(m+1)] for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(1, m+1):
            for p in range(max(0, i-k), i):
                if dp[i][j] > dp[p][j-1] + cost[i]:
                    dp[i][j] = dp[p][j-1] + cost[i]
                    path[i][j] = path[p][j-1] + [p]

   
    return dp[n-1][m], path[n-1][m]


n, k, m = map(int, input().split())
cost = list(map(int, input().split()))


min_cost, min_cost_path = min_cost_to_cross_river(n, cost, k, m)
print(" ".join(map(str, min_cost_path)))