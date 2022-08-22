N = int(input())

num_list = []
for _ in range(N):    # 차례대로 입력 받아주기
    num_list.append(int(input()))



for i in range(N-1):  # 선택정렬 정의 (시간초과로 실패)
    minidx = i
    for j in range(i+1, N):
        if num_list[minidx] > num_list[j]:
            minidx = j
        num_list[i], num_list[minidx] = num_list[minidx], num_list[i]

# num_list.sort()로 정렬해서 돌리면 통과됨

for _ in num_list:
    print(_)
    

