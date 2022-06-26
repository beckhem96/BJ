import sys

def bfs(i, j):
    q = [(i, j)]
    while q:
        si, sj = q.pop()
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
            ni, nj = si + di, sj + dj
            if 0<=ni<H and 0<=nj<W and not v[ni][nj] and arr[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj))

while 1:
    W, H = map(int, input().split())
    if W == 0 and H ==0:
        sys.exit(0)
    arr = []
    for _ in range(H):
        arr.append(list(map(int, input().split())))
    v = [[0]*W for _ in range(H)]

    cnt = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] and not v[i][j]:
                v[i][j] = 1
                bfs(i, j)
                cnt += 1
    print(cnt)