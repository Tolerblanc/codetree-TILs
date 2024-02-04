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
result = 0
for x, v, i in vertical:
    if v == 1:
        checker.add(i)
        continue
    result = max(result, len(checker))
    checker.remove(i)
print(result)