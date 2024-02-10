import sys
input = sys.stdin.readline


def lower_bound(lst, target):
    left, right = 0, len(lst) - 1
    lb = n
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            lb = min(lb, mid)
        if lst[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return lb + 1 if lb != n else -1


n, m = map(int, input().split())
nums = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    print(lower_bound(nums, q))