import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, len(nums)):
    if nums[i - 1] == 0:
        cnt += 1
        nums[i - 1] = 1
        nums[i] = 1 - nums[i]
        if i + 1 < len(nums):
            nums[i + 1] = 1 - nums[i + 1]
print(cnt if all(nums) else -1)