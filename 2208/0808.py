# BOJ 14696 딱지놀이

for i in range(int(input())):
    A, *a = list(map(int, input().split()))
    B, *b = list(map(int, input().split()))
    # 좀 더 스마트하게 입력값을 받을 수 있는 방법은 없을까? 가변인자!
    
    
    # 딱지의 종류가 4개가 아닐 때는 어떻게 비교할 수 있을까?
    # count 함수를 쓰면 0값이 출력되므로 쉽게 비교할 수 있다.
    if a.count(4) > b.count(4):
        print('A')
    elif a.count(4) < b.count(4):
        print('B')
    else:
        if a.count(3) > b.count(3):
            print('A')
        elif a.count(3) < b.count(3):
            print('B')
        else:
            if a.count(2) > b.count(2):
                print('A')
            elif a.count(2) < b.count(2):
                print('B')
            else:
                if a.count(1) > b.count(1):
                    print('A')
                elif a.count(1) < b.count(1):
                    print('B')
                else:
                    print('D')
            