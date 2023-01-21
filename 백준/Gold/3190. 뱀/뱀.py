import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input())
arr = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    ai, aj = map(int, input().split())
    arr[ai-1][aj-1] = 1 # 사과있는데에 1표시
L = int(input())
directions = dict()
for _ in range(L):
    n, c = input().split()
    directions[int(n)] = c
# 처음에는 오른쪽을 보고 있음 (동, 남, 서, 북)
d = [[0,1],[1,0],[0,-1],[-1,0]]

i, j = 0, 0
arr[i][j] = 2 #뱀있는데는 2
direction = 0
seconds = 0
q = [(i, j)]
def turn(c):
    global direction
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
while 1:
    seconds += 1
    ni, nj = i+d[direction][0], j+d[direction][1]
    if 0 > ni or N<= ni or 0 > nj or N<=nj:
        break
    if arr[ni][nj] == 1:
        arr[ni][nj] = 2
        q.append((ni, nj))
    elif arr[ni][nj] == 0:
        arr[ni][nj] = 2
        q.append((ni, nj))
        exi, exj = q.pop(0)
        arr[exi][exj] = 0
    else:
        break
    i, j = ni, nj
    if seconds in directions:
        turn(directions[seconds])

print(seconds)
