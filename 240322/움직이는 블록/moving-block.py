n = int(input())
blocks = [int(input()) for _ in range(n)]
avg = sum(blocks) // n
print(sum([max(avg - block, 0) for block in blocks]))