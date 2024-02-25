n = int(input())
arr=[]
cnt = 0


def beautiful(depth):
    global cnt
    if depth == n:
        cnt += 1
    if depth > n:
        return

    for i in range(1, 5):
        if len(arr)+i<=n:
            for _ in range(i):
                arr.append(i)
            beautiful(depth + i)
            for _ in range(i):
                arr.pop()


beautiful(0)
print(cnt)