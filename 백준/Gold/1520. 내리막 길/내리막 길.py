import sys
import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
dp = [[-1] * N for _ in range(M)]
def dfs(i, j):
    if i == M-1 and j == N-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    ways = 0
    for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
        ni, nj = i + di, j + dj
        if 0<=ni<M and 0<=nj<N and arr[i][j] > arr[ni][nj]:
            ways += dfs(ni,nj)
    dp[i][j] = ways
    return dp[i][j]

print(dfs(0, 0))