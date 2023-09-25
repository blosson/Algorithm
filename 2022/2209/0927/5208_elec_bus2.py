def min_cnt(idx, cnt):                              # idx는 정류장의 리스트 index (실제 정류장 번호 - 1), cnt는 충전 횟수
    global ans

    if ans <= cnt:                                  # 현재까지의 최소 충전횟수가 현재 충전횟수보다 작거나 같으면 뒤는 거른다.
        return

    if idx >= N - 1:                                # 마지막 정류장에 도착하면 비교한 후 return 
        if ans > cnt:
            ans = cnt
        return

    for i in range(chargers[idx], 0, -1):           # 현재 정류장의 갈 수 있는 거리만큼을 뒤쪽부터 순회 (이렇게 하면 더 빠를 것 같아서..)
        min_cnt(idx + i, cnt + 1)                   # 다음 정류장 인덱스 넣어주기 /  충전 횟수 1 더해주기 

T = int(input())
for tc in range(1, T + 1):
    N, *chargers = map(int, input().split())        # 정류장 수랑 충전지 따로 구분해서 입력 받아주기
    ans = float('inf')                              # 무한히 큰 값 (정답 변수)

    min_cnt(0, -1)                                  # 0번 인덱스 출발, 처음 정류소에서는 충전한 걸로 치지 않으므로 cnt는 -1로 조정해주기
    print(f'#{tc} {ans}')

        
    
    