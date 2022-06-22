def nCr(n, r, s):   # n개에서 r개를 고르는 조합. s 고를 수 있는 구간의 시작 인덱스
    if r==0:
        print(*sorted(p))
    else:
        for i in range(s, n-r+1):
            p[r-1] = a[i]
            nCr(n, r-1, i+1)

N, M = map(int, input().split())

a = []
p = [0] * M
u = [0] * N
for i in range(1, N+1):
    a.append(i)

# perm(0, M, N)
nCr(N, M, 0)