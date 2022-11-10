C = int(input())
for _ in range(C):
    N, *scores = map(int, input().split())
    average = sum(scores) / len(scores)
    
    cnt = 0
    for score in scores:
        if score > average:
            cnt += 1
    
    # ratio = round(cnt / N * 100, 3)
    ratio = cnt / N * 100
    print(f'{ratio :0.3f}%')