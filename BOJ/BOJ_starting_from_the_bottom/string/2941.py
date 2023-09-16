# 다른 사람들은 list의 replace를 사용했는데 나는 set와 여러 조건을 줘서 같은 시간이 걸렸다.
# 이렇게 다양하게 사고해보는 연습 나쁘지 않은 것 같다.

croatia_set_len2 = {'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='}
croatia_set_len3 = {'dz='} 
word = input()

cnt = len(word)
for s in croatia_set_len2:
    for i in range(len(word) - 1):
        if s in word[i:i+2]:
            if s == 'z=':
                if i != 0 and word[i-1] == 'd':
                    pass
                else:
                    cnt -= 1
            else:
                cnt -= 1

for s in croatia_set_len3:
    for i in range(len(word) - 2):
        if s in word[i:i+3]:
            cnt -= 2

print(cnt)

        
            

