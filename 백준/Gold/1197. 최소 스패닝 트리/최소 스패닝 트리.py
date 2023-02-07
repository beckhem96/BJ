import sys
input = sys.stdin.readline

V, E = map(int, input().split())
uf = [i for i in range(V+1)]
mst = 0
arr = [list(map(int, input().split())) for _ in range(E)]
arr.sort(key=lambda x:x[2]) # 가중치가 작은 순으로 정렬

def find(x):
    if uf[x] == x:
        return x
    root_node = find(uf[x])
    uf[x] = root_node
    return root_node

def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y
for u, v, w in arr:
    if find(u) != find(v): # 루트 노드가 다르면
        mst += w # 가중치 더함
        union(u, v)

print(mst)