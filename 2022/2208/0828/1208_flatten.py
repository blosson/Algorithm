for tc in range(1, 11):

    N = int(input())
    boxes = list(map(int, input().split()))

    n = 1
    while n <= N: 
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        n += 1

    print(f'#{tc} {(max(boxes) - min(boxes))}')


