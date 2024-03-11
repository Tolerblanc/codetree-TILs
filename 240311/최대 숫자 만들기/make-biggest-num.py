from functools import cmp_to_key


def compare(x, y):
    a = int(str(x) + str(y))
    b = int(str(y) + str(x))
    if a < b:
        return 1
    elif a > b:
        return -1
    return 0


n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(key=cmp_to_key(compare))
print(''.join(map(str,nums)))