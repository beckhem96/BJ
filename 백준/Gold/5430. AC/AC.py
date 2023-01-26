import sys
# import heapq
from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    task = input().strip()
    N = int(input())
    arr = input().strip()[1:-1].split(',')
    q = deque(arr)
    reverse_flag = 0
    error_flag = 0
    if not N:
        q = []
    for cmd in task:
        if cmd == 'R':
            reverse_flag += 1
        elif cmd == "D":
            if len(q) < 1:
                error_flag = 1
                print('error')
                break
            else:
                if reverse_flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if error_flag == 0:
        if reverse_flag % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')