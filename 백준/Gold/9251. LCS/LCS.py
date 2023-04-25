import sys
# import copy
# from collections import deque
# sys.setrecursionlimit(10**9)
input = sys.stdin.readline
strA = list(input().strip())
strB = list(input().strip())
n, m = len(strA), len(strB)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if strA[i-1] == strB[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])