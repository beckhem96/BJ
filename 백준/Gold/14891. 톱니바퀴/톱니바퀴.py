import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

arr = []
tasks = []
result = 0
for _ in range(4):
    arr.append(list(map(int, list(input().strip()))))

k = int(input())
for _ in range(k):
    tasks.append(tuple(map(int, input().split())))

for n, w in tasks:
    q = [(n-1, w)] # 몇 번째 톱니 바퀴인지
    task = [(n-1, w)] # 돌릴 톱니 바퀴 리스트
    visited = [0, 0, 0, 0]
    visited[n-1] = 1
    while q: # 4개 톱니바퀴에서 맞닿아 있는 부분이 다른 거 찾기

        i, dw = q.pop(0)
        for di in [1, -1]:
            ni = i + di
            if 0<=ni<4 and di == -1 and arr[i][6] != arr[ni][2] and not visited[ni]:
                task.append((ni, -dw))
                q.append((ni, -dw))
                visited[ni] = 1
            elif 0<=ni<4 and di == 1 and arr[i][2] != arr[ni][6] and not visited[ni]:
                task.append((ni, -dw))
                q.append((ni, -dw))
                visited[ni] = 1
    for a, b in task:
        if b == 1:
            arr[a] = [arr[a][-1]] + arr[a][:-1]
        else:
            arr[a] = arr[a][1:] + [arr[a][0]]

for i in range(4):
    if arr[i][0] == 1:
        result += 2**i
print(result)
