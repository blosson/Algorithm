N = int(input())
line_list = list(map(int, input().split()))

ans_list = []
for i in range(N):
    if line_list[i] != 0:          
        ans_list.insert(-line_list[i], i+1)   # insert(-i, value)에서 -1은 뒤에서 첫 번째 인덱스 바로 앞에 value를 삽입하라는 뜻
    else:
        ans_list.append(i+1)                  # line_list[i] 값이 0일 때는 제일 뒤에 줄을 서므로 그냥 append로 추가

print(*ans_list)



    