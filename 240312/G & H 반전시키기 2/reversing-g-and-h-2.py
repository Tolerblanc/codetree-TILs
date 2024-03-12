import sys
input = sys.stdin.readline

n = int(input())
init = input().rstrip()
comp = input().rstrip()

cnt = 0
stat = False # 뒤에서 부터 볼건데, 이전에 스위치가 눌렸는지 여부
for i in range(n - 1, -1, -1):
    if stat and init[i] == comp[i] or not stat and init[i] != comp[i]:
        cnt += 1
        stat = not stat
print(cnt)