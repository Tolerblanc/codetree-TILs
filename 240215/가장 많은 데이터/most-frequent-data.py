from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())
print(Counter(lst).most_common()[0][1])