import sys
input = sys.stdin.readline

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if not graph[i][j]:
            blank.append((i, j))

def check_col(y, a):
    for i in range(9):
        if graph[y][i] == a:
            return False
    return True
def check_row(x, a):
    for i in range(9):
        if graph[i][x] == a:
            return False
    return True

def check_rectangle(y, x, a):
    ny = y//3*3
    nx = x//3*3
    for i in range(3):
        for j in range(3):
            if graph[ny+i][nx+j] == a:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    for i in range(1, 10):
        y = blank[idx][0]
        x = blank[idx][1]
        if check_col(y, i) and check_row(x, i) and check_rectangle(y, x, i):
            graph[y][x] = i
            dfs(idx+1)
            graph[y][x] = 0
dfs(0)