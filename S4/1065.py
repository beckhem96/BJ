#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 핵심은 1의 자리, 2의 자리 수는 모두 한수다
# 서로 뺴면 등차가 1개이기 때문
N = int(input())
if 0 < N < 100: # 1~99
    result = N
else: # 100 ~ 999
    result = 99
    for num in range(100, N+1):
        num = str(num)
        if int(num[1]) - int(num[0]) == int(num[2]) - int(num[1]):
            result += 1
print(result)