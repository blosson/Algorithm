import sys
sys.stdin = open('1208.txt', 'r')

for tc in range(1, 11):

    dump = int(input())
    boxes = list(map(int, input().split()))

    hmax = 0            # 최댓값
    hmax_index = -1     # 최댓값 index
    hmin = 101          # 최솟값
    hmin_index = 100    # 최솟값 index

    for d in range(dump):

        for i in range(100):
            if boxes[i] > hmax:
                hmax = boxes[i]
                hmax_index = i

            if boxes[i] < hmin:
                hmin = boxes[i]
                hmin_index = i

        boxes[hmax_index] -= 1     
        boxes[hmin_index] += 1
        hmax -= 1
        hmin += 1

    ans = hmax - hmin
    print(f'#{tc} {ans}')




















'''def findMax(boxes) : # 배열에서 값이 가장 큰 인자의 인덱스와 그 값 반환하는 함수
    maxV = 0
    for i in range(100) :
        if boxes[i] > maxV :
            maxV = boxes[i]
            maxI = i
    return maxI, maxV # 최대값 인덱스, 최대값

def findMin(boxes) : # 배열에서 값이 가장 작은 인자의 인덱스와 그 값 반환하는 함수
    minV = 101
    for i in range(100) :
        if boxes[i] < minV :
            minV = boxes[i]
            minI = i
    return minI, minV # 최소값 인덱스, 최소값

for t in range(10) :
    dump = int(input())
    boxes = [int(b) for b in input().split()]

    while dump > 0 : # 가능한 덤프 횟수동안
        boxes[findMax(boxes)[0]] -= 1 # 가장 큰 값 -1
        boxes[findMin(boxes)[0]] += 1 # 가장 작은 값 +1
        dump -= 1
    print(f'#{t + 1} {findMax(boxes)[1] - findMin(boxes)[1]}')'''