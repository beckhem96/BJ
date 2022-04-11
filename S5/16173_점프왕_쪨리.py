N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
v = [[0] * N for _ in range(N)]

q.append((0, 0))
while q:
    i, j = q.pop(0)
    if arr[i][j] == -1:
        print('HaruHaru')
        exit(0)
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = i + di*arr[i][j], j + dj*arr[i][j]
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
            v[ni][nj] = 1 # v로 방문표시 안해주면 시간초과남...
            q.append((ni, nj))
print('Hing')