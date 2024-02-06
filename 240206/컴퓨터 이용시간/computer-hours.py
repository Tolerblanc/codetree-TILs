import sys
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    p, q = map(int, input().split())
    points.append((p, 1, i))
    points.append((q, -1, i))
points.sort()
answer = [0] * n

checker = set() # i번 컴퓨터 사용중
com = dict() # key 유저가 value 컴퓨터 사용 중
pSum = 0
for x, v, i in points:
    pSum += v
    if v == 1:
        if pSum in checker:
            for j in range(1, n + 1):
                if j not in checker:
                    answer[i] = j
                    checker.add(j)
                    com[i] = j
                    break
        else:
            answer[i] = pSum
            com[i] = pSum
            checker.add(pSum)
    else:
        checker.remove(com[i])

print(*answer)