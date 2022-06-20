def BFS(pi, pj):
    q = []
    q.append((pi, pj))
    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj))


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    cnt = 0
    v = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not v[i][j]:
                v[i][j] = 1
                BFS(i, j)
                cnt += 1
    print(cnt)