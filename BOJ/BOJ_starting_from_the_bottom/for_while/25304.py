total = int(input())
N = int(input())

check = 0
for _ in range(N):
    price, n = map(int, input().split())
    check += (price * n)

if total == check:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)