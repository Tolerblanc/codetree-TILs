import sys
input = sys.stdin.readline

n = int(input())
checkpoints = []
for _ in range(n):
    checkpoints.append(tuple(map(int, input().split())))


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


distances = [0]
for i in range(1, n):
    distances.append(distances[-1] + manhattan(checkpoints[i], checkpoints[i - 1]))

rev_distances = [0]
for i in range(n-1, 0, -1):
    rev_distances.append(rev_distances[-1] + manhattan(checkpoints[i - 1], checkpoints[i]))
rev_distances.reverse()

answer = distances[-1]
for i in range(1, n-1):
    answer = min(answer, distances[i - 1] + rev_distances[i + 1] + \
         manhattan(checkpoints[i + 1], checkpoints[i - 1]))
print(answer)