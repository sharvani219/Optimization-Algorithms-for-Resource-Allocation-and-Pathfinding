from collections import deque

def min_cost_to_cross_river(n, cost, k):
    dp = [0] * n
    parent = [-1] * n
    dp[0] = cost[0]

    dq = deque()
    dq.append(0)

    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()

        dp[i] = cost[i] + dp[dq[0]]
        parent[i] = dq[0]

        while dq and dp[i] <= dp[dq[-1]]:
            dq.pop()

        dq.append(i)

    min_cost_to_cross = float('inf')
    last_platform = -1
    for j in range(n-1, max(n-k, 0)-1, -1):
        if dp[j] < min_cost_to_cross:
            min_cost_to_cross = dp[j]
            last_platform = j

    path = []
    while last_platform != -1:
        path.append(last_platform)
        last_platform = parent[last_platform]

    return min_cost_to_cross, path[::-1]

# Read input
n, k = map(int, input().split())
cost = list(map(int, input().split()))

# Call the function
min_cost, path = min_cost_to_cross_river(n, cost, k)

# Print output

for platform in path:
    print(platform, end=" ")
print()
