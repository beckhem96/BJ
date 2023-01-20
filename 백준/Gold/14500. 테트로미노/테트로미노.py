import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

case_1 = [[[0, 0], [0, 1],[0, 2], [0, 3]],
          [[0, 0],[1, 0], [2, 0], [3, 0]],
          [[0, 0], [1, 0], [2, 0], [2, 1]],
          [[0, 0], [1, 0], [2, 0], [2, -1]],
          [[0, 0], [1, 0], [0, 1], [0, 2]],
          [[0, 0], [1, 0], [0, -1], [0, -2]],
          [[0, 0], [1, 0], [1, 1], [1, 2]],
          [[0, 0], [1, 0], [1, -1], [1, -2]],
          [[0, 0], [0, 1], [1, 1], [2, 1]],
          [[0, 0], [0, 1], [1, 0], [2, 0]],
          [[0, 0],[1, 0], [0, 1], [1, 1]],
          [[0, 0],[1, 0], [1, 1], [2, 1]],
          [[0, 0],[1, 0], [1, -1], [2, -1]],
          [[0, 0],[0, 1], [1, 1], [1, 2]],
          [[0, 0],[0, -1], [1, -1], [1, -2]],
          [[0, 0],[-1, 0], [0, -1], [0, 1]],
          [[0, 0],[1, 0], [0, -1], [0, 1]],
          [[0, 0],[1, 0], [-1, 0], [0, 1]],
          [[0, 0],[1, 0], [-1, 0], [0, -1]]
          ]
# case_2 = [
#         [[0, 0],[1, 0], [2, 0], [2, 1]],
#         [[0, 0],[1, 0], [2, 0], [2, -1]],
#         [[0, 0],[1, 0], [0, 1], [0, 2]],
#         [[0, 0],[1, 0], [0, -1], [0, -2]],
#         [[0, 0],[1, 0], [1, 1], [1, 2]],
#         [[0, 0],[1, 0], [1, -1], [1, -2]],
#         [[0, 0],[0, 1], [1, 1], [2, 1]],
#         [[0, 0],[0, 1], [1, 0], [2, 0]]
#     ]
# case_3 = [[0, 0],[1, 0], [0, 1], [1, 1]]
# case_4 = [[[0, 0],[1, 0], [1, 1], [2, 1]],
#           [[0, 0],[1, 0], [1, -1], [2, -1]],
#           [[0, 0],[0, 1], [1, 1], [1, 2]],
#           [[0, 0],[0, -1], [1, -1], [1, -2]]]
# case_5 = [[[0, 0],[-1, 0], [0, -1], [0, 1]],
#           [[0, 0],[1, 0], [0, -1], [0, 1]],
#           [[0, 0],[1, 0], [-1, 0], [0, 1]],
#           [[0, 0],[1, 0], [-1, 0], [0, -1]]]
def find_max(i, j):
    global result
    for case in case_1:
        arr_sum = 0
        for di, dj in case:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M:
                arr_sum += arr[ni][nj]
            else:
                break
        result = max(result, arr_sum)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        find_max(i, j)
print(result)