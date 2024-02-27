import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def backtracking(depth, selected):
    if depth == m:
        print(*result)
        return
    for i in range(selected + 1, n + 1):
        result.append(i)
        backtracking(depth + 1, i)
        result.pop()


backtracking(0, 0)