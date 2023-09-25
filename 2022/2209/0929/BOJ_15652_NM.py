'''
1. 중복 조합으로 전체 경우의 수를 가져오는 함수를 만든다.
2. 그 안에서 백트래킹으로 잔가지들을 쳐낸다.
'''

def dfs(start):
    if len(arr) == M:                   # M이 되면 리스트가 꽉 찼으므로 출력
        print(*arr)
        return
    
    for i in range(start, N):           # 인덱스 순회
        arr.append(i+1)                 # start가 0이므로 1부터 넣을수 있도록 인덱스 조정
        dfs(i)
        arr.pop()                       # 리스트가 꽉차면 뒤에서부터 다시 빼주고 순회

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]    # 부터 N까지 차례대로 있는 리스트 생성
arr = []                                # 중복좋바 넣을 리스트

dfs(0)





