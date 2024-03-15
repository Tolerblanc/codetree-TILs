import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

r = 0
prefix = 0
ans = 4242424242
for l in range(len(nums)):
    while r < len(nums) and prefix < s:
        prefix += nums[r]
        r += 1
    ans = min(ans, r - l + 1)
    prefix -= nums[l]
print(ans)