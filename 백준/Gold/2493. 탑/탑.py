import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input())
tops = list(map(int, input().split()))
stack = []
result = []
for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i, tops[i]])

for ans in result:
    print(ans, end=' ')