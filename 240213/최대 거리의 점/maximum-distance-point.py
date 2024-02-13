import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = []
for _ in range(n):
    points.append(int(input()))
points.sort()

def check(dist):
    cnt = 1
    prev = points[0]
    for point in points[1:]:
        if point - prev >= dist:
            prev = point
            cnt += 1
    return cnt >= m


answer = 0
left, right = 0, 1000000000
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)