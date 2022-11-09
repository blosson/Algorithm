N = int(input())
numbers = list(map(int, input().split()))
V = int(input())

cnt = 0
for number in numbers:
    if number == V:
        cnt += 1

print(cnt)
