import sys
import heapq
input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    points.append((x1, 1, y, i))
    points.append((x2, -1, y, i))
points.sort()

check = set() # 인덱스 셋
height = [] # (y, i) 힙, 0번이 지금 맨 앞에 있는 선분
answer = 0
for x, v, y, i in points:
    if v == 1: # 시작점이면
        if not check: # 기존에 시작한 선분이 없다면
            answer += 1
        elif height and height[0][0] > y: # 지금 선분이 더 가까이 있다면
            answer += 1
        heapq.heappush(height, (y, i)) # 힙에 추가
        check.add(i)

    else: #끝점이면
        check.remove(i)
        if height[0][1] == i: # 만약 제거 대상이 맨 앞에 있던 선분이라면
            heapq.heappop(height)
            while height and height[0][1] not in check: # 맨 앞에 있는 선분이 check에 없으면 제거:
                heapq.heappop(height)
            answer += 1

print(answer - 1) # 맨 마지막에 체크된건 제거해줘야함