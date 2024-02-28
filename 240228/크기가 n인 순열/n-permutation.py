import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
result = []


def backtracking(depth):
    if depth == n:
        print(*result)
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True 
        result.append(i)
        backtracking(depth + 1)
        result.pop()
        visited[i] = False


backtracking(0)