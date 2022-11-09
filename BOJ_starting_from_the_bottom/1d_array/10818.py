N = int(input())
numbers = list(map(int, input().split()))

max_num = -1000000
min_num = 1000000
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(min_num, max_num)