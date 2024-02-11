import sys
input = sys.stdin.readline


def game(m, target):
    left, right = 1, m
    cnt = 0
    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        if mid == target:
            return cnt
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


answer = [1000000000, -1000000000]
m = int(input())
a, b = map(int, input().split())
for target in range(a, b + 1):
    curr = game(m, target)
    answer[0] = min(curr, answer[0])
    answer[1] = max(curr, answer[1])
print(*answer)