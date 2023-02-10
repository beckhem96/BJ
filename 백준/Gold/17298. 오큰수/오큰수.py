import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
# from collections import deque
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = [] # 스택에 인덱스 넣고, 못 찾으면 보류

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


for r in answer:
    print(r, end=' ')