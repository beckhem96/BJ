import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

dp = [[0]*201 for _ in range(201)]

for i in range(1, 201):
    for j in range(1, 201):
        if i == 1:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        elif i > 1 and j > 1:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[K][N] % 1000000000)