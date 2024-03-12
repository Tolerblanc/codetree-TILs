import sys
input = sys.stdin.readline

n = int(input())
init = input().rstrip()
comp = input().rstrip()

ans = 0
stat = True # 이전 상태
for s1, s2 in zip(init, comp):
    if stat and s1 != s2:
        ans += 1
    stat = s1 == s2
print(ans)