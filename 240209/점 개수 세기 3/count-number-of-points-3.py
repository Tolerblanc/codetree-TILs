import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
comp = {k:v for v, k in enumerate(nums)}

for _ in range(q):
    a, b = map(int, input().split())
    print(comp[b] - comp[a] + 1)