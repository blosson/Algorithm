test_case = int(input()) # test case 입력

n = 1 # test case 만큼 반복
while n <= test_case:
    how_many = int(input()) # 숫자 몇개나 넣을거니
    numbers = list(map(int, input().split())) # 숫자 입력

    king = numbers[0] # king : 가장 큰 수 (일단 index 0부터 시작해서 비교)
    for i in numbers: # for 문을 돌려서 
        if i > king: # numbers[i] 값이 king보다 크면
            king = i # king에 새로운 값 할당


    slave = numbers[0] # slave = 가장 작은 수 (일단 index 0부터 시작해서 비교)
    for j in numbers: # for 문을 돌려서 
        if j < slave: # numbers[i] 값이 slave보다 작으면
            slave = j # slave 에 새로운 값 할당

    max_diff = king - slave # 최댓값과 최솟값 차이 (둘다 양의 정수이므로 절댓값 필요없음)
    print(f'#{n} {max_diff}')

    n += 1