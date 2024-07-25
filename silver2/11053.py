# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))

result = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[j] + 1, result[i])

print(max(result))
