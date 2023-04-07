N, M = map(int, input().split())

boxes = [0] * N

for i in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        boxes[idx-1] = k
    
print(*boxes)
    
    
