import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]


def check(limit):
    cnt = 0
    for time in times:
        cnt += limit // time
    return cnt >= n

answer = 10 ** 16
left, right = 0, 10 ** 16
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1
print(answer)