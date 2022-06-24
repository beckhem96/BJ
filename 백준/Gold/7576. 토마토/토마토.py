import sys

def f():
    global cnt
    while q:
        while q:
            day.append(q.pop())
        while day:
            i, j = day.pop()
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i + di, j + dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    q.append((ni, nj))
        cnt += 1

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
confirm = 0
for i in range(N):
    if 0 not in arr[i]:
        confirm += 1
if confirm == N:
    print(0)
    sys.exit(0)
q = []
day = []
cnt = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
f()
for i in range(N):
    if 0 in arr[i]:
        print(-1)
        sys.exit(0)
print(cnt)