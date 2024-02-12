import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))


def check(divider, minimum):
    result = 0
    for num in nums:
        result += num // divider
    return result >= minimum


answer = 0
left, right = 1, 100000
while left <= right:
    mid = (left + right) // 2
    if check(mid, m):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)