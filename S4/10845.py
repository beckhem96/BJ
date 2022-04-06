# 큐
import sys

sys.stdin = open('10485_input.txt', 'r')

N = int(input())
input_list = []
for _ in range(N):
    input_list.append(input().split())
q = []
front = 0
back = -1
while input_list:
    pop_v = input_list.pop(0)
    if pop_v[0] == 'push':
        q.append(int(pop_v[1]))
    elif pop_v[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif pop_v[0] == 'size':
        print(len(q))
    elif pop_v[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif pop_v[0] == 'front':
        if q:
            print(q[front])
        else:
            print(-1)
    elif pop_v[0] == 'back':
        if q:
            print(q[back])
        else:
            print(-1)

