n = int(input())
nums = [1, 1]

for _ in range(2, n):
    nums.append(nums[-1] + nums[-2])

print(nums[-1])