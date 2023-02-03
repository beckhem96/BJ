import sys
import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
N = int(input())
w = []
w_b = []
dp = [0 for i in range(N)]
for i in range(N):
    w.append(list(map(int, input().split())))
w.sort(key=lambda x:x[0])
for i in range(N):
    w_b.append(w[i][1])
for i in range(N): # 왜 부분 수열이냐 오름 차순이면 교차하지 않는다!
    #  그래서 최대의 오름차순 관계를 갖는 값들을 계산하는 것!
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N - max(dp))

