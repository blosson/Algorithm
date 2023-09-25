def pascal(N):
    pascal_list = [1] * N       # 빈 스트 만들어주기
    if N <= 2:
        return pascal_list      # 1과 2의 경우 1밖에 없으니 그냥 return
    
    else:
        for i in range(1, N - 1):                               # 양끝은 1이므로 범위에서 제외
            pascal_list[i] = pascal(N-1)[i-1] + pascal(N-1)[i]  # 재귀함수 (이거 어려우니 복습하자..)
        return pascal_list

for tc in range(1, int(input()) + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N+1):     # pascal()은 해당 줄만 출력하므로 for문 이용
        print(*pascal(i))       # * : list 벗겨주고 , 없애준다!