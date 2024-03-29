def f(n, k, m):    # 순열 p[n]을 채우는 함수. k 고를 개수, m 주어진 숫자 개수
    if n==k:
        print(*p, sep=' ')
    else:
        for i in range(m): # used에서 사용하지 않은 숫자 검색
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 표시
                p[n] = arr[i]     # p[n] 결정
                f(n+1, k, m)
                used[i] = 0     # a[i]를 다른 위치에서 사용할 수 있도록 함
    return

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
p = [0] * M
used = [0] * N
f(0, M, N)