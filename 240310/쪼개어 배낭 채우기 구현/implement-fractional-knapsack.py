import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
jewels.sort(key=lambda x: -x[1] / x[0])

cost = 0
for jewel in jewels:
    if m >= jewel[0]:
        cost += jewel[1]
        m -= jewel[0]
    else:
        cost += (jewel[1] / jewel[0]) * m
        break
print(f'{cost:.3f}')