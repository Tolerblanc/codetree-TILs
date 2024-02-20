from collections import Counter
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cc = Counter(list(map(int, input().split())))

answer = 0
for num in cc.keys():
    if num == k - num:
        answer += cc[num] * (cc[k - num] - 1)
        continue
    answer += cc[num] * cc[k - num]
print(answer // 2)