n, m = map(int, input().split())
people = list(map(int, input().split()))

answer = 0
prev = -1
prev 
for i, p in enumerate(people):
    if p == 0:
        continue
    if prev == -1 or prev + m < i:
        prev = i + m
        answer += 1
print(answer)