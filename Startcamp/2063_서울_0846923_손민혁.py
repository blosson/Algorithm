'''import random

N = int(input())
x = [random.randint(0, 101) for x in range(0, N)]
x.sort()

#print(x)
#print(x[(N-1)//2]) # 왜 /로 하면 에러가 뜨고 //로 하면 정상 작동할까?

y = int((N-1)/2)
print(x[y])'''


N = int(input())
a = list(map(int, input().split())) # 이 의미를 정확히 이해 못하겠다. 공부 필요

a.sort()
k = int((N-1)/2)
print(a[k])
