import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dists = list(map(int, input().split()))
answer = 0
score = [0] * k


def backtracking(depth):
    global answer
    if depth == n:
        answer = max(answer, len([s for s in score if s >= m]))
        return
    
    for i in range(len(score)):
        score[i] += dists[depth]
        backtracking(depth + 1)
        score[i] -= dists[depth]


backtracking(0)
print(answer)