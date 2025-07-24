def brute_force(sn, k, cost, m):
    if m < 0 or sn < 0:
        return float("inf"), []
    if sn == 0 and m == 0:
        return 0, []
    
    mi = float("inf")
    mp = []
    for i in range(1, k + 1):
        cc, pp = brute_force(sn - i, k, cost, m - 1)
        if cc is not None and (sn - i) >= 0:
            cc += cost[sn - i]
            if cc < mi:
                mi = cc
                mp = pp + [sn - i]

    return mi, mp

n, k, m = map(int, input().split())
cost = list(map(int, input().split()))
result_cost, result_path = brute_force(n, k, cost, m)
final_path = ' '.join(map(str, result_path))
print(final_path)