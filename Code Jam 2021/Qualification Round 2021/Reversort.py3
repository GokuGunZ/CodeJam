def solve(t):
    N = input()
    ls = list(map(int, input().split()))
    
    ans = 0
        
    while len(ls) > 1:
        ls, n = dotti(ls)
        ans += n
        ls = ls[1:]
        
    print("Case #"+str(t+1)+": "+str(ans))

def dotti(ls):
    m = min(ls)
    i = ls.index(m)
    l1 = ls[:i+1]
    l2 = ls[i+1:]
    l1 = l1[::-1]
    
    return l1+l2, i+1

T = int(input())
for t in range(T):
    solve(t)