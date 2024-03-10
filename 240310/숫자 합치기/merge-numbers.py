import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
heapq.heapify(nums)

cost = 0
while len(nums) >= 2:
    curr = heapq.heappop(nums) + heapq.heappop(nums)
    heapq.heappush(nums, curr)
    cost += curr
print(cost)