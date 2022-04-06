# DFS
# def maze(i, j, cnt):
#     global result
#     if i == n and j == m:
#         if result > cnt:
#             result = cnt
#     elif result < cnt:
#         return
#     else:
#         for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
#                 v[ni][nj] = 1
#                 maze(ni, nj, cnt+1)
#                 v[ni][nj] = 0
#
#
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# n, m = N-1, M-1 # 배열 도착지
# v = [[0]*M for _ in range(N)] # 방문기록, 없으면 계속 돌아서 distance가 많아짐
# starti, startj = 0, 0
# v[startj][startj] = 1
# result = 999999
# maze(starti, startj, 1)
# print(result)

# BFS
def maze(q):
    while q:
        i, j = q.pop(0) # 앞에 있는거 먼저 꺼내서

        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]: # 델타 탐색
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                # 범위 안벗어나고 갈 수 있는 길이면
                q.append([ni, nj]) # 다음 길 넣어주고
                arr[ni][nj] = arr[i][j] + 1 # i, j에서 현재 길보다 한칸 더 간거 표시

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
n, m = N-1, M-1 # 배열 도착지
v = [[0]*M for _ in range(N)] # 방문기록, 없으면 계속 돌아서 distance가 많아짐
q = [[0, 0]]
result = 999999
v[0][0] = 1
maze(q)
print(arr[n][m])