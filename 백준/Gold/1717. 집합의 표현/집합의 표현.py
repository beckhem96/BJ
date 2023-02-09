import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x): # 루트 찾기
    if uf[x] == x: # 루트가 자신이다
        return x
    root_node = find(uf[x]) # 정점 자신이 루트가 아니면 루트의 루트를 찾음
    uf[x] = root_node # 찾은 루트 초기화
    return root_node

def union(x, y):
    X, Y = find(x), find(y) # 두 값의 루트를 찾고
    uf[X] = Y # 하나의 루트로 합쳐줌

for _ in range(m):
    task, a, b = map(int, input().split())
    if task == 0:
        if find(a) != find(b):
            union(a, b)
    elif task == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')