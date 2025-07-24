def find(sn, k, cost, memo):  # sn is the step number
    if sn == 0:
        return 0, []
    if sn < 0:
        return float("inf"), []
    if (sn, k) in memo:
        return memo[(sn, k)]

    path = []
    mi = float("inf")
    mp = []
    for i in range(1, k + 1):
        pc, pp = find(sn - i, k, cost, memo)
        if pc != float("inf") and (sn - i) >= 0:
            cc = pc + cost[sn - i]
            if cc < mi:
                mi = cc
                mp = pp + [sn - i]
    memo[(sn, k)] = mi, mp
    return memo[(sn, k)]

n, k = map(int, input().split())
cost = list(map(int, input().split()))
result_cost, result_path = find(n, k, cost, {})
final_path = ' '.join(map(str, result_path))
print(final_path)