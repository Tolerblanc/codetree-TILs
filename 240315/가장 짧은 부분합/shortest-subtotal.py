import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

r = 0
prefix = nums[-0]
ans = 4242424242424242
for l in range(n):
    while r + 1 <= n - 2 and prefix < s:
        prefix += nums[r + 1]
        r += 1
    if prefix < s:
        break
    ans = min(ans, r - l + 1)
    prefix -= nums[l]
print(ans if ans != 4242424242424242 else -1)