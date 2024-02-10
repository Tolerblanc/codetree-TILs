from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(m):
    target = int(input())
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(mid + 1)
            break
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if left > right:
        print(-1)