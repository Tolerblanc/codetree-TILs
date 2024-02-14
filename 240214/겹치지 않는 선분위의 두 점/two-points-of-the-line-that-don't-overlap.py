import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()

def check(dist):
    cnt = 0
    prev = lines[0][0]
    for start, end in lines:
        if prev > end:
            continue
        if prev < start:
            prev = start
        cnt += (end - prev) // dist + 1
        prev += (end - prev) // dist

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