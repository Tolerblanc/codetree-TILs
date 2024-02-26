import sys
input = sys.stdin.readline

k, n = map(int, input().split())
selected = []

def backtracking(depth):
    if depth == n:
        print(*selected)
        return
    
    for i in range(1, k + 1):
        if len(selected) >= 3 and selected[-1] == selected[-2] == i:
            continue
        selected.append(i)
        backtracking(depth + 1)
        selected.pop()

backtracking(0)