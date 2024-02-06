import sys
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    a, b = map(int, input().split())
    points.append((a, 1, i))
    points.append((b, -1, i))
points.sort()

checker = set()
prev = 0
answer = 0
for x, v, i in points:
    if v == 1:
        if not checker:
            prev = x
        checker.add(i)
    else:
        checker.remove(i)
        if not checker:
            answer = max(answer, x - prev)
print(answer)