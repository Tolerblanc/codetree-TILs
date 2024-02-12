import sys
input = sys.stdin.readline

s = int(input())
left, right = 1, s
answer = 0
while left <= right:
    mid = (left + right) // 2
    if (mid + 1) * mid // 2 <= s:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)