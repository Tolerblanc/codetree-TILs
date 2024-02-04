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
l, result = 0, 0
for x, v, i in vertical:
    if v == 1:
        checker.add(i)
        continue
    if len(checker) > l:
        result = 1
        l = len(checker)
    elif len(checker) == l:
        result += 1
    checker.remove(i)
print(result)