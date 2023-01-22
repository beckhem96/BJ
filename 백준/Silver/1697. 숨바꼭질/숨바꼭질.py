import sys
# import heapq
from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

q = deque()
q.append(N)
while 1:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in [x - 1, x + 1, x * 2]:
        if 0<=nx<=MAX and not dist[nx]:
            dist[nx] = dist[x] + 1
            q.append(nx)