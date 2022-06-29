def bfs(si, sj):
    q = []
    q.append((si, sj))
    while q:
        i, j = q.pop(0)
        if i == li and j == lj:
            return v[i][j]
        for di, dj in [[2, -1], [2, 1], [1, -2], [1, 2], [-2, 1], [-2, -1], [-1, -2], [-1, 2]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                v[ni][nj] = v[i][j] + 1
                q.append((ni, nj))



T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    li, lj = map(int, input().split())
    if si == li and sj == lj:
        print(0)
        continue
    v = [[0]*N for _ in range(N)]
    print(bfs(si, sj))