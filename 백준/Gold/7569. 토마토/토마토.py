import sys
# import heapq
from collections import deque
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

M, N, H = map(int, input().split())
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if -1<nx<N and -1<ny<M and -1<nz<H and data[nz][nx][ny] == 0:
                data[nz][nx][ny] = data[z][x][y] + 1
                queue.append((nz, nx, ny))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

result = -2
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result, data[i][j][k])
print(result - 1)