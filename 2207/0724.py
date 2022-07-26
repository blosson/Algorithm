
while True:
    number = int(input())
    if number > 100000:
        print('100,000 이하의 숫자를 입력하세요.') # 아래줄이 아니라 바로 옆줄에 입력할 수 있게 하는 방법?
    else:
        break

print('#' * number)