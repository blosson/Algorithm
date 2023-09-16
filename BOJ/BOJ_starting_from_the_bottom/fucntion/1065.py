N = int(input())

cnt = 0
for i in range(1, N+1):
    num = str(i)
    num_len = len(num)

    if len(num) <= 2:
        cnt += 1

    else:
        check = True
        diff = int(num[0]) - int(num[1])
        for i in range(num_len - 1):
            if diff != int(num[i]) - int(num[i+1]):
                check = False
                break
        
        if check == True:
            cnt += 1
            
print(cnt)


        
        