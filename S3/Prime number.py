M, N = map(int, input().split()) # 에라토스테네스의 체, 배수들을 거르고 걸르는 것?
arr = [1] * (N+1)
for i in range(2, int(N**0.5)+1): # N의 제곱근 까지만
    if arr[i]:
        for j in range(i*2, N+1, i): # 배수들을 0으로 저장
            arr[j] = 0
for i in range(M, len(arr)):
    if i > 1 and arr[i]:
        print(i)
# 참고 블로그
# https://leejunggae.tistory.com/3
