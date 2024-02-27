import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
answer = 0


def get_xor(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result |= number
    return result


def backtracking(depth, selected):
    global answer
    if depth == m:
        answer = get_xor(result)
        return
    for i in range(selected + 1, n):
        result.append(nums[i])
        backtracking(depth + 1, i)
        result.pop()


backtracking(0, 0)
print(answer)