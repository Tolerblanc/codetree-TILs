from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = Counter(list(map(int, input().split())))
queries = list(map(int, input().split()))
print(*[nums[query] for query in queries])