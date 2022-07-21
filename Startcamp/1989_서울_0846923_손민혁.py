T = int(input())    

for t in range(1, T+1): # range랑 for문 공부를 더 해야겠다. 검색해볼 생각조차 못했다.
    word = input()
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            print('#%i'%t, 1) #이런식으로 표현하는 것도 더 공부해야겠다..
        else:
            print('#%i'%t, 0)
            break # break도 사용법 더 알아보자. 기초 너무 부족하네 ㅠ
        break

'''v = list('hellobello')

l = len(v)
print(l)
if v[0] == v[k-1]:
    if v[1] == v[k-2]:
        if v[2] == v[k-3]:s
            if v[3] == v[k-4]:
                if v[4] == v[k-5]:
                    print('#1 1')
                else:
                    print('#1 0')
            else:
                    print('#1 0')
        else:
                    print('#1 0')
    else:
                    print('#1 0')
else:
                    print('#1 0')'''