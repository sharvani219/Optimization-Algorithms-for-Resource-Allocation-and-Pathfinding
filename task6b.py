n, k, m = map(int, input().split())
cost = list(map(int, input().split()))
dp = [[[float("inf"), []] for i in range(m + 1)] for j in range(n + 1)]
dp[0][0] = [0, []]

for l in range(1, m + 1):
    for i in range(1, n + 1):
        for j in range(max(0, i - k), i):
            if dp[j][l - 1][0] + cost[j] < dp[i][l][0]:
                dp[i][l][0] = dp[j][l - 1][0] + cost[j]
                dp[i][l][1] = dp[j][l - 1][1] + [j]
result = ' '.join(map(str, dp[n][m][1]))
print(result)