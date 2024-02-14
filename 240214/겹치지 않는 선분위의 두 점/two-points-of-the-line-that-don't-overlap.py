import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()

def check(dist):
    cnt = 1
    prev = lines[0][0]
    for start, end in lines:
        if prev + dist > end:
            continue
        if prev + dist < start:
            prev = start
            cnt += 1
        dots = max((end - prev) // dist, 0)
        cnt += dots
        prev += dots * dist
    return cnt >= n

answer = 0
left, right = 1, 10 ** 18
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)