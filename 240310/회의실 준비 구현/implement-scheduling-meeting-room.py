import sys
input = sys.stdin.readline

n = int(input())
conferences = [tuple(map(int, input().split())) for _ in range(n)]
conferences.sort(key=lambda x: x[1])

prev = conferences[0][1]
cnt = 1
for s, e in conferences[1:]:
    if prev <= s:
        prev = e
        cnt += 1
print(cnt)