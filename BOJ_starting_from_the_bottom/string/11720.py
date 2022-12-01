N = int(input())
number = int(input())
str_number = str(number)

number_list = list(map(int, str_number))

ans = 0
for number in number_list:
    ans += number

print(ans)