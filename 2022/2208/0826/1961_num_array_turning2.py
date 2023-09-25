# 함수로 구현 버전 (아름답다..)

def turning90(arr, N):
    spin90 = []
    for i in range(N):
        plus_list = []
        for j in range(N):
            plus_list.append(arr[N-1-j][i])         # 90도 회전시키는 방법
        spin90.append(plus_list)
    return spin90

for tc in range(1, int(input()) + 1):
    

    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    spin90 = turning90(numbers, N)                  # 90도 회전
    spin180 = turning90(spin90, N)                  # 180도 회전 (90 * 2)
    spin270 = turning90(spin180, N)                 # 270도 회전 (90 * 3)

    print(f'#{tc}')
    for i in range(N):
        print(*spin90[i], sep = '', end = ' ')      # *, sep 개념 이해해서 따로 출력 (join-map도 사용가능하단 걸 잊지말자!)
        print(*spin180[i], sep = '', end = ' ')
        print(*spin270[i], sep = '')

        


