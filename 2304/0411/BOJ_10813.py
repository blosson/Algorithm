N, M = map(int, input().split())
boxes = [0] * N

# box에 공 넣기 (1번 box부터 시작이므로 idx + 1)
for i in range(N):
    boxes[i] = i+1

# for문 돌려서 pythonic 하게 공 교환 
for i in range(M):
    a, b = map(int, input().split())
    boxes[a-1], boxes[b-1] = boxes[b-1], boxes[a-1]

print(*boxes)
    
    
    