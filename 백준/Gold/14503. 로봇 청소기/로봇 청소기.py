import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# 0: 북, 1: 동, 2: 남, 3: 서
dr = [-1, 0, 1, 0] # r이 세로
dc = [0, 1, 0, -1] # c가 가로
N, M = map(int, input().split()) #
r, c, d = map(int, input().split()) #
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
result = 1
while 1:
    flag = 0 # 새롭게 이동한 곳에서 청소했는지 안했는지 표시
    for _ in range(4):
        d = (d+3)%4 # 이게 제일 중요함
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            result += 1
            # 이동
            r = nr
            c = nc
            flag = 1
            break
    if flag == 0: # 4방향 모두 청소X
        if arr[r-dr[d]][c-dc[d]]:
            print(result)
            break
        else:
            r, c = r - dr[d], c - dc[d]
