from itertools import permutations 

def solve(t):
    N, C = list(map(int, input().split()))
    
    if C > N*(N+1)/2 or C < N-1:
        print("Case #"+str(t+1)+": IMPOSSIBLE")
        return
    
    ls = list(range(1,N+1))
    #print(ls)
    for p in permutations(ls):
        p2 = p[:]
        #print(p, cost(p))
        if cost(p) == C:
            print("Case #"+str(t+1), end=': ')
            for i in p2:
                print(i, end=' ')
            print()
            return
    print("Case #"+str(t+1)+": IMPOSSIBLE")

def cost(ls):
    ans = 0
    while len(ls) > 1:
        ls, n = reversort(ls)
        ans += n
        ls = ls[1:]
    return ans

def reversort(ls):
    m = min(ls)
    i = ls.index(m)
    l1 = ls[:i+1]
    l2 = ls[i+1:]
    l1 = l1[::-1]
    
    return l1+l2, i+1

T = int(input())
for t in range(T):
    solve(t)