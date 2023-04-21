# BOJ_2563 색종이 (S5)

num = int(input())
paper = [[0] * 100 for _ in range(100)]

# 10*10의 색종이의 x, y 좌표값을 기반으로 순회해서 리스트의 idx값을 0->1로 바꿔줌
for _ in range(num):
    width, height = map(int, input().split())
    for i in range(width, width+10):
        for j in range(height, height+10):
            paper[i][j] = 1

# 전체 paper 순회해서 1인 부분이 있으면 넓이에 더해줌
ans = 0                      
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            ans += 1

print(ans)

ans = 0
for row in paper:
    ans += row.count(1)


            
