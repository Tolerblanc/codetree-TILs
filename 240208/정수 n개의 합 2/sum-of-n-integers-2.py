import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [nums[0]]
for i in range(1, n):
    prefix.append(prefix[-1] + nums[i])

answer = 0
for i in range(n-k+1):
    answer = max(answer, prefix[i + k - 1] - prefix[i] + nums[i])
print(answer)