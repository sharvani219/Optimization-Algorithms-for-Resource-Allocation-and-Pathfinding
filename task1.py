def brute_force(sn, cost, k):
    if sn == 0:
        return 0, []
    if sn < 0:
        return float("inf"), []

    mi = float("inf")
    mp =  float("inf")
    for i in range(1, k + 1):
        pc, pp = brute_force(sn - i, cost, k)
        if pc is not None and (sn - i) >= 0:
            cc = pc + cost[sn - i]
            if cc < mi:
                mi = cc
                mp = pp + [sn - i]

    return mi, mp

n, k = map(int, input().split())
cost = list(map(int, input().split()))
result_cost, result_path = brute_force(n, cost, k)
result_path = ' '.join(map(str, result_path))
print(result_path)





















