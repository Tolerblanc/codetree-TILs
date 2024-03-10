n = int(input())
nums = list(map(int, input().split()))

prefix = 0
for num in nums:
    if prefix < 0:
        prefix = 0
    prefix += num
print(prefix)