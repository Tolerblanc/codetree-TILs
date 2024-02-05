import sys
input = sys.stdin.readline

n, k = map(int, input().split())
points = []
curr = 0
for _ in range(n):
    v, d = input().split()
    v = int(v)
    if d == 'L': #왼쪽
        points.append((curr, -1))
        points.append((curr - v, 1))
        curr -= v
    else: # 오른쪽
        points.append((curr, 1))
        points.append((curr + v, -1))
        curr += v
points.sort()

pSum = 0
answer = 0
for x, v in points:
    if v == 1:
        pSum += 1
        if pSum >= k:
            prev = x
    else:
        if pSum == k:
            answer += abs(prev - x)
        pSum -= 1
print(answer)