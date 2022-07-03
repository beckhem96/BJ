def nCr(n, r, s):
    global result

    if r==0:
        sum_distance = 0
        for i in range(len(homes)):
            si, sj = homes[i]
            home_chicken_distance = 99999999
            for j in range(len(comb)):
                ti, tj = comb[j]
                if home_chicken_distance > (abs(si - ti) + abs(sj - tj)):
                    home_chicken_distance = (abs(si - ti) + abs(sj - tj))
            sum_distance += home_chicken_distance
        if result > sum_distance:
            result = sum_distance
    else:
        for i in range(s, n-r+1):
            comb[r-1] = chickens[i]
            nCr(n, r-1, i+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
comb = [0] * M
homes = []
chickens = []
result = 1000000
chicken_num = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i, j))
        if arr[i][j] == 2:
            chickens.append((i, j))
            chicken_num += 1


nCr(chicken_num, M, 0)
print(result)