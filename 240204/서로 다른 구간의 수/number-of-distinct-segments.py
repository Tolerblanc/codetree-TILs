import sys
input = sys.stdin.readline

n = int(input())
vertical = []
for i in range(n):
    a, b = map(int, input().split())
    vertical.append((a, 1, i))
    vertical.append((b, -1, i))
vertical.sort()
checker = set()

answer = 0
for x, v, i in vertical:
    if v == 1:
        if not checker:
            answer += 1
        checker.add(i)
    else:
        checker.remove(i)
print(answer)