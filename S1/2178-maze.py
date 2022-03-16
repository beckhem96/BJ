def maze(i, j, top):
    i, j = stack[top]
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
            stack.append((ni, nj))
            top += 1
            v[ni][nj] = 1
            if ni == n and nj == m:
                result.append(top)
            maze(ni, nj, top)
            stack.pop()
            top -= 1
            v[ni][nj] = 0

    return 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
n, m = N-1, M-1 # 배열 도착지
top = -1
v = [[0]*M for _ in range(N)] # 방문기록, 없으면 계속 돌아서 distance가 많아짐
stack = []
starti, startj = 0, 0
stack.append((starti, startj))
v[startj][startj] = 1
top += 1
result = []
maze(starti, startj, top)
print(min(result)+1)
