# https://www.acmicpc.net/problem/2606
n = int(input())    # 1~100
dic = { i+1: set([i+1]) for i in range(n)}

# Input
pair_cnt = int(input())
for i in range(pair_cnt):
    src, tar = map(int, input().split())

    neighbors = dic[src] | dic[tar]     # union
    for j in neighbors:
        dic[j] = neighbors

print(len(dic[1]) - 1)
