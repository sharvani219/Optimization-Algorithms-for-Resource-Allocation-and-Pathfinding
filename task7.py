import heapq

def min_cost_to_cross_river(n, cost, k, m):
    dp = [[float('inf')] * (m+1) for _ in range(n+1)]
    dp[0][0] = 0
    path = [[[] for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n):
        for j in range(1, m+1):
            min_heap = []
            for p in range(max(0, i-k), i):
                heapq.heappush(min_heap, (dp[p][j-1] + cost[i], p))
            min_cost, min_index = heapq.heappop(min_heap)
            dp[i][j] = min_cost
            path[i][j] = path[min_index][j-1] + [min_index]

    return path[n-1][m]


n, k, m = map(int, input().split())
cost = list(map(int, input().split()))


min_cost_path = min_cost_to_cross_river(n, cost, k, m)

print(" ".join(map(str, min_cost_path)))