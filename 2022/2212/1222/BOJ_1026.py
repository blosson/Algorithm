#108ms

'''
B의 위치는 가만히 있고 A의 순서만 바꿀 수 있다고 해도 어차피 A와 B 하나씩 곱해서 더하는거니 B의 위치를 바꾸어도 상관없다! 
따라서 가장 B의 수와 가장 작은 A의 수가 만나서 곱한 뒤 더할 수 있게 해주자는 아이디어를 떠올림.
그래서 A는 오름차순 정렬, B는 내림차순 정렬해서 각각 더해줌 (반대도 상관 X)
'''

N = int(input())                                # 숫자 갯수
a_nums = list(map(int, input().split()))        # A 숫자들
b_nums = list(map(int, input().split()))        # B 숫자들

a_nums.sort()                                   # 오름차순 정렬
b_nums.sort(reverse=True)                       # 내림차순 정렬

ans = 0                                         # 정답 변수 (합의 최솟값)
for i in range(N):
    ans += (a_nums[i] * b_nums[i])              # 각각 곱해서 ans에 더해준다.

print(ans)

