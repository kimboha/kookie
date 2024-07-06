# https://www.acmicpc.net/problem/2839
n = int(input())
answer = -1
x = 0
y = int(n / 5)

while y >= 0:
    mod = n - (y * 5)

    if mod % 3 == 0:
        x = int(mod / 3)
        answer = x + y
        break

    y -= 1

print(answer)
