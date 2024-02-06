import sys
import heapq
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    p, q = map(int, input().split())
    points.append((p, 1, i))
    points.append((q, -1, i))
points.sort()
answer = [0] * n

pSum = 0
coms = [i for i in range(1, n + 1)]
heapq.heapify(coms)
for x, v, i in points:
    pSum += v
    if v == 1:
        answer[i] = heapq.heappop(coms)
    else:
        heapq.heappush(coms, answer[i])

print(*answer)