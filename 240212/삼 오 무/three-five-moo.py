import sys
input = sys.stdin.readline

n = int(input())

answer = 1 << 31
left, right = 0, 1 << 31
while left <= right:
    mid = (left + right) // 2 # 1 ~ mid 안쪽에 숫자가 몇 개 있는가?
    cnt = mid - (mid // 3) - (mid // 5) + (mid // 15)
    if cnt >= n:
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1
print(answer)