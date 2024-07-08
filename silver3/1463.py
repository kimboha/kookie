# https://www.acmicpc.net/problem/1463
n = int(input())
g_costs = { 1: 0, 2: 1 }

# Main
for i in range(3, n + 1):
    costs = [
        g_costs[i//3] + 1 if i % 3 == 0 else i,
        g_costs[i//2] + 1 if i % 2 == 0 else i,
        g_costs[i-1] + 1
    ]
    g_costs[i] = min(costs)

print(g_costs[n])
