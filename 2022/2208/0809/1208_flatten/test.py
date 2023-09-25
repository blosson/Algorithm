

dump = int(input())
boxes = list(map(int, input().split()))
hmax = 0
hmax_index = -1
hmin = 101
hmin_index = 10
for d in range(dump):
    for i in range(10):
        if boxes[i] > hmax:
            hmax = boxes[i]
            hmax_index = i
        if boxes[i] < hmin:
            hmin = boxes[i]
            hmin_index = i
    boxes[hmax_index] -= 1
    print(boxes[hmax_index])     
    boxes[hmin_index] += 1
    hmax -= 1
    print(hmax)
    hmin += 1
ans = hmax - hmin
print(f'# {ans}')

        
     
        
