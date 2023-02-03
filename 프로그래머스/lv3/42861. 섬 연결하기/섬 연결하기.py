import sys
import heapq

# def get_parent(c, node):
#     if c[node] == node:
#         return node
#     else:
#         root_node = get_parent(c, node)
#         c[node] = root_node
#     return root_node

# def union_find(c, edge):
#     p1 = get_parent(c, edge[1])
#     p2 = get_parent(c, edge[2])
    
#     if not p1 == p2: # 루트가 같지 않으면 사이클이 아님
#         if p1 > p2: # 더 큰 노드를
#             c[p1] = p2
#         else:
#             c[p2] = p1
#         return edge[0]
#     return 0
def find(uf, x):
    if uf[x] == x:
        return x
    root_node = find(uf, uf[x])
    uf[x] = root_node
    return root_node
def union(x, y, uf):
    a = find(uf, x)
    b = find(uf, y)
    uf[a] = b
    
def solution(n, costs):
    ans = 0
    mst = []
    costs.sort(key = lambda x : x[2])
    uf = [x for x in range(n)]
    
    for cost in costs:
        u, v, w = cost
        if find(uf, u) != find(uf, v):
            mst.append(cost)
            union(u, v, uf)
    for a, b, c in mst:
        ans += c
    return ans
                
        
        