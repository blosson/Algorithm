N, country = map(int, input().split())

result = []                                     # 전체 국가의 결과
for _ in range(N):
    medals = list(map(int, input().split()))
    result.append(medals)
    
    if medals[0] == country:                    # 내가 랭킹을 알고싶은 국가의 메달 정보라면
        country_result = medals                 # 변수에 넣어줌 (궁금한 국가의 메달 정보)

gold = country_result[1]                        # 금은동 편의상 변수 설정
silver = country_result[2]
bronze = country_result[3]

# print(country_result)

olympic_rank = 1                                # 기본적으로 1등부터 시작 (0이 아님에 주의)
for medal in result:                            # for문 돌리면서 금은동 갯수로 순위 매겨줌
    if medal[1] > gold:
        olympic_rank += 1
    
    elif medal[1] == gold:
        if medal[2] > silver:
            olympic_rank += 1
        
        elif medal[2] == silver:
            if medal[3] > bronze:
                olympic_rank += 1

print(olympic_rank)
        




