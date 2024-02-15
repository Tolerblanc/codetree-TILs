import sys
input = sys.stdin.readline

d = {}

n = int(input())
for _ in range(n):
    inp = input().split()
    if inp[0] == 'add':
        d[inp[1]] = inp[2]
    elif inp[0] == 'find':
        print(d.get(inp[1], None))
    else:
        d.pop(inp[1], None)