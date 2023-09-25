T = int(input()) # 테스트 케이스 개수

n = 1 # T만큼 반복하기 위한 개수
while  n <= T:
    all_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 0부터 9까지 존재하는 리스트
    add_list = [] # 추가할 리스트
    N = input()
    # 1 <= int(N) <= 1000000 이건 나중에 조건 만들자
    k = 1 # 곱한 횟수
    while True:
        NN = str(int(N) * k) # 양의 번호
        for i in NN: 
            if int(i) in all_list: # i값이 all_list에 있는지 확인
                add_list.append(int(i)) # 있으면 add_list 추가
                add_list = list(set(add_list)) # 중복값 없애고 정렬(근데 이거 자동 정렬 왜 되는거지?)

        if add_list == all_list: # 두 리스트가 같으면
            print(f'#{n} {int(NN)}')
            break
        k = k + 1
    n = n + 1


# list -> set -> list 과정에서 왜 오름차순으로 정렬이 되는지?

'''a = [4, 5, 1, 3]
a = set(a)
print(a)
a = list(a)
print(a)

if [1, 3, 4, 5] == [3, 4, 5, 1]: # 둘은 다름. 안의 값들은 같지만 리스트 순서가 다르기 때문에.
    print(True)
else:
    print(False)'''


