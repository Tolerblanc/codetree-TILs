from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(m):
    target = int(input())
    print(bisect_right(nums, target) - bisect_left(nums, target))