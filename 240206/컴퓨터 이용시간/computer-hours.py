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

coms = [i for i in range(1, n + 1)]
heapq.heapify(coms)
for _, v, i in points:
    if v == 1:
        answer[i] = heapq.heappop(coms)
    else:
        heapq.heappush(coms, answer[i])

print(*answer)