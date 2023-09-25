arr = [5, 321, 11, 215, 53]

# 1 iteration
def SelectionSort(arr):
    n = len(arr)

    if n == 1:
        return
    
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[min_i], arr[i] = arr[i], arr[min_i] # 자기자신과 같은 경우에도 if문 쓰는 것보다 이렇게 그냥 바꾸는 게 나음

# 2 recursion
def Recursion_SelectionSort(arr, s):            # s는 정렬 시작 지점
    n = len(arr)

    if s == n - 1:                              # s가 마지막 인덱스에 다다르면 정렬 종료
        return

    min_i = s                                   # 기본 최소 idx를 s로 잡아줌
    for i in range(s, n):
        if arr[min_i] > arr[i]:                 
            min_i = i
    arr[s], arr[min_i] = arr[min_i], arr[s]     # 최소값이 인덱스s에 올 수 있게

    Recursion_SelectionSort(arr, s + 1)         # 재귀로 다음 함수 호출

Recursion_SelectionSort(arr, 0)
print(arr)

    
    


