k, n = map(int, input().split())


def backtracking(depth, result):
    if depth == n:
        print(*result)
        return
    
    for i in range(1, k + 1):
        result.append(i)
        backtracking(depth + 1, result)
        result.pop()


backtracking(0, [])