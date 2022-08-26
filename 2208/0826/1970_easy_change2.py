for tc in range(1, int(input()) + 1):

    money = int(input())
    m50000 = m10000 = m5000 = m1000 = m500 = m100 = m50 = m10 = 0
    
    
    if (money // 50000) >= 1:
        m50000 += (money // 50000)
        money %= 50000
    
    if (money // 10000) >= 1:
        m10000 += (money // 10000)
        money %= 10000
    
    if (money // 5000) >= 1:
        m5000 += (money // 5000)
        money %= 5000
    
    if (money // 1000) >= 1:
        m1000 += (money // 1000)
        money %= 1000
    
    if (money // 500) >= 1:
        m500 += (money // 500)
        money %= 500
    
    if (money // 100) >= 1:
        m100 += (money // 100)
        money %= 100
    
    if (money // 50) >= 1:
        m50 += (money // 50)
        money %= 50
    
    if (money // 10) >= 1:
        m10 += (money // 10)
        money %= 10
    
    print(f'#{tc}')
    print(m50000, m10000, m5000, m1000, m500, m100, m50, m10)
