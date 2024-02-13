import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

answer = 10 ** 10
left, right = 1, 10**10
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, mid // i) # i번째 행에는 i의 배수, n 보다 커질 수 없음
    if cnt >= k:
        answer = min(mid, answer)
        right = mid - 1
    else:
        left = mid + 1
print(answer)