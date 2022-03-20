N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*2)] # v*2는 신청인 수와 정원, v*2+1는
for i in range(N):
    print(arr[i*2])
    print(arr[i*2+1])