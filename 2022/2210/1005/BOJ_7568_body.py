# 근데 자신과키가 같고 몸무게는 더 많은 사람은 자신보다 덩치가 클 수 있다고 할 수 있지 않나?
# 이런 테스트 케이스는 없는듯..?

N = int(input())
body_spec = [list(map(int, input().split())) for _ in range(N)]
rank_list = []                      # 자신의 순위를 담을 리스트

for self in body_spec:              # 자기 자신의 스펙 순회
    cnt = 1                         # 기본 등수는 1로 설정
    for others in body_spec:        # 다른 사람의 스펙 순회 & 키, 몸무게가 자신보다 더 크면
        if others[0] > self[0] and others[1] > self[1]:
            cnt += 1                # 등수가 하나씩 밀려남
    rank_list.append(cnt)           # 다른 사람과 비교가 끝나면 자신의 등수 리스트에 추가

print(*rank_list)