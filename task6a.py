def find(sn, k, cost, m, memo):  # sn is the step number
    if m < 0 or sn < 0:
        return None, None
    if (sn, m) in memo:
        return memo[(sn, m)]
    if sn == 0 and m == 0:
        return 0, []
    path = []
    mi = float("inf")
    mp = []
    for i in range(1, k + 1):
        pc, pp = find(sn - i, k, cost, m - 1, memo)
        if pc is not None and (sn - i) >= 0:
            cc = pc + cost[sn - i]
            if cc < mi:
                mi = cc
                mp = pp + [sn - i]
    memo[(sn, m)] = mi, mp
    return memo[(sn, m)]


input_line = input().strip()
n, k, m = map(int, input_line.split())
cost = list(map(int, input().split()))


result_cost, result_path = find(n, k, cost, m, {})
final_path = ' '.join(map(str, result_path))
print(final_path)