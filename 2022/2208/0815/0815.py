def BubbleSort(a, N):                                       # a : list
    for i in range(N-1, 0, -1):                             # Bubblesort 응용
        for j in range(0, i):
            if len(a[j]) > len(a[j+1]):                     # 길이가 더 길면 자리 바꿈
                a[j], a[j+1] = a[j+1], a[j]            
            if len(a[j]) == len(a[j+1]) and a[j] > a[j+1]:  # 사전순 정렬
                a[j], a[j+1] = a[j+1], a[j]
    return a

N = int(input())

words = []
for i in range(N):
    words.append(input())
words = list(set(words))      # 중복값 제거

BubbleSort(words, N)

for i in range(N):
    print(words[i])








#hello = []
#hello[0] = 123  이거 불가능!