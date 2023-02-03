import sys
import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] == 0 and graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1
for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()