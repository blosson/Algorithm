def pascal(N):
    L = [1]*N  # 양 옆이 1 이니까
    if N == 1 :
        return L
    if N == 2 :
        return L # 2일때는 1만 두 개니까 
    else :
				# 인덱스 0은 무조건 1이고 인덱스 N-1도 무조건 1이니까 범위를 1부터 N-2로 설정
        for i in range(1,N-1):
						# 직전 수에대한 pascal 함수를 불러오면서 현재 idx와 그 전 idx의 합을 저장
            L[i] = pascal(N-1)[i] + pascal(N-1)[i-1]
				# 리스트를 리턴해서 리스트를 다시 불러올 수 있게함
        return L

for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1}')
		# pascal함수는 한 줄만 리턴하므로 삼각형 출력을 위해 for문을 돌려줌
    for i in range(1,N+1):
        print(*pascal(i))