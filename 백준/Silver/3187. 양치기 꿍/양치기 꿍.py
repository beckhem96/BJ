def bfs(i, j):
    global wolves, sheep
    q = [(i, j)]
    while q:
        si, sj = q.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = si + di, sj + dj
            if 0<=ni<R and 0<=nj<C and not v[ni][nj] and arr[ni][nj] != '#':
                v[ni][nj] = 1
                q.append((ni, nj))
                if arr[ni][nj] == 'k':
                    sheep += 1
                elif arr[ni][nj] == 'v':
                    wolves += 1


R, C = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]
v = [[0] * C for _ in range(R)]
result = [0, 0]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v' and not v[i][j]:
            wolves, sheep = 1, 0
            v[i][j] = 1
            bfs(i, j)
            if wolves >= sheep:
                result[1] += wolves
            elif wolves < sheep:
                result[0] += sheep

        elif arr[i][j] == 'k' and not v[i][j]:
            sheep, wolves = 1, 0
            v[i][j] = 1
            bfs(i, j)
            if wolves >= sheep:
                result[1] += wolves
            elif wolves < sheep:
                result[0] += sheep
print(*result)