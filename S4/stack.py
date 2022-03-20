N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
stack = []
top = -1
for i in range(len(arr)):
    if arr[i][0] == 'push':
        stack.append(int(arr[i][1]))
        top += 1
    elif arr[i][0] == 'pop':
        if stack:
            print(stack.pop())
            top -= 1
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[top])
        else:
            print(top)
