import sys
input = sys.stdin.readline

n = int(input())
vertical = []
for _ in range(n):
    s, e = map(int, input().split())
    vertical.append((s, 1))
    vertical.append((e, -1))
vertical.sort()

pSum = 0
answer = 0
for x, v in vertical:
    pSum += v
    answer = max(answer, pSum)
print(answer)