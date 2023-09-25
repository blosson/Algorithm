arr = [1, 4, 0, 2, 1, 3, 1, 2]          # 정렬할 배열
result = [0] * len(arr)                 # 정렬된 결과를 출력할 배열
k = max(arr)                            # arr의 원소중 최댓값(0도 있으니 아래서 k+1 만큼의 counts 배열을 생성함)

def Counting_Sort(arr, result, k):
    counts = [0] * (k + 1)              # 갯수를 셀 counts 배열 생성 (0도 포함해야하기 때문에 k+1)

    for i in range(0, len(arr)):        # arr 원소가 총 몇 번 나오는지 counts 리스트 각 인덱스에 기록
        counts[arr[i]] += 1

    for i in range(1, len(counts)):     # index 0은 이미 자기 값이 입력되어 있으므로 1부터 시작
        counts[i] += counts[i-1]        # 이전까지의 합과 자기자신을 더한 값을 입력 (자기 자신을 포함해 총 몇개가 있는지에 대한 값)
        
    for i in range(len(result)-1, -1, -1):   # 뒤에서부터 읽어오는 이유는 같은 숫자라도 순서를 그대로 유지하기 위해서 (=안정정렬)
        counts[arr[i]] -= 1                  # counts에서 해당 인덱스 값에 -1을 해주고 (먼저 하는 이유는 counts값은 갯수니까 인덱스 값에 입력을 위해서는 -1을 해주어야 함)
        result[counts[arr[i]]] = arr[i]      # result의 인덱스 자리에 arr[i] 값을 입력

    return result                            # 정렬 완료!

print(Counting_Sort(arr, result, k))

    