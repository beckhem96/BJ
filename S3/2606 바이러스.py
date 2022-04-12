def dfs(s):
    v[s] = 1
    for i in arr[s]:
        if not v[i]:
            dfs(i)



N = int(input())
M = int(input())
arr = [[] * N for _ in range(N+1)] #
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
v = [0] * (N+1)
dfs(1)
print(v.count(1)-1)
