def normal(i, j, RGB):
    v[i][j] = 1
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0<=ni<T and 0<=nj<T and not v[ni][nj] and arr[ni][nj] == RGB:
            normal(ni, nj, arr[ni][nj])

def unnormal(i, j, RGB, color_list):
    v[i][j] = 1
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0<=ni<T and 0<=nj<T and not v[ni][nj] and arr[ni][nj] in color_list:
            unnormal(ni, nj, arr[ni][nj], color_list)

import sys
sys.setrecursionlimit(5000)

T = int(input())
arr = [list(input()) for _ in range(T)]
v = [[0]*T for _ in range(T)]
normal_area = 0
unnormal_area = 0
unnormal_color = ['R', 'G']

for i in range(T):
    for j in range(T):
        if not v[i][j]:
            v[i][j] = 1
            normal(i, j, arr[i][j])
            normal_area += 1

v = [[0]*T for _ in range(T)]

for i in range(T):
    for j in range(T):
        if not v[i][j] and arr[i][j] in unnormal_color:
            unnormal(i, j, arr[i][j], unnormal_color)
            unnormal_area += 1
        elif not v[i][j] and arr[i][j] not in unnormal_color:
            unnormal(i, j, arr[i][j], ['B'])
            unnormal_area += 1

print(normal_area, unnormal_area)