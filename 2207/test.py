'''list = ['-', '-', '-']

print(*list)'''

T = int(input()) #테스트케이스 개수
test_list = [] #일괄출력하고자 한다 -> 알려주신거 

for i in range(1, T+1): #1부터 테스트케이스까지를 
    N = int(input())
    a,b,c,d,e = 0,0,0,0,0
    test_list_2 = []
    
    if N%2 ==0: #2로 나눠진다면
        while N%2 ==0: #2로 나누는 걸 계속 하고
            N = N/2 #나눌때마다 한번씩 더 2로 나누고 
            a = a+1 #그럴때마다 test_list_2리스트의 a에 1씩 추가한다.
    test_list_2.append(a)

    if N%3 ==0:
        while N%3 ==0:
            N = N/3
            b = b+1
    test_list_2.append(b)

    if N%5 ==0:
        while N%5 ==0:
            N = N/5
            c = c+1
    test_list_2.append(c)

    if N%7 ==0:
        while N%7 ==0:
            N = N/7
            d = d+1
    test_list_2.append(d)

    if N%11 ==0:
        while N%11 ==0:
            N = N/11
            e = e+1
    test_list_2.append(e)
    test_list.append(test_list_2) #이걸 추가했더니 거의 정답에 가까워졌다.
	
    for j in range(len(test_list)): 
        print(f'#{j+1}', end=' ')
        print(*test_list[j])  