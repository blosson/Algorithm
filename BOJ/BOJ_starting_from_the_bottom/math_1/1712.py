A, B, C = map(int, input().split())

if B >= C:                              # 한 대당 생산비용이 판매 가격보다 크면 당연히 손익분기점을 넘을 수 없으므로 당연히 -1
    ans = -1

else:                                   # while문에서 1씩 증가시켜 손익분기점을 확인해보려 했으나 숫자가 어마무시하게 커지는 순간 시간이 너무 오래걸림
    # cnt = 1
    # while True:
    #     print(A / (C - B))
    #     if cnt > A / (C - B):
    #         print('yes')
    #         ans = cnt
    #         break
    #     cnt += 1

    ans = int(A / (C - B)) + 1          # 따라서 분기점이 되는 정확한 해를 구하고 int로 씌워준 뒤 +1를 해주면 이익이 발생하는 수량 ans가 나옴

print(ans)