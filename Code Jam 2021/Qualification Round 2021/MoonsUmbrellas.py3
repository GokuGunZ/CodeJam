def dalf(t):
    X, Y, S = input().split()
    X = int(X)
    Y = int(Y)
    
    ans = 0
    last = ''
    for c in S:
        if c != last and c != '?':
            if last == 'C':
                ans += X
            elif last == 'J':
                ans += Y
            last = c
    
    print(f"Case #{t+1}: {ans}")
    


T = int(input())
for t in range(T):
    dalf(t)