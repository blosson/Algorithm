arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]

count_list = [0] * (max(arr) + 1)   # 0도 포함되어 있으므로 정수의 최댓값 +1 만큼의 길이가 필요함

for num in arr:
    count_list[num] += 1            # num 원소가 총 몇 번 나오는지 count 리스트에 기록

for i in range(1, len(count_list)): # index 0은 이미 자기값이 입력되어 있으므로 1부터 시작
    count[i] += count[i-1]          # 이전까지의 합과 자기자신을 더한 값을 입력


    