def solve(t):
    n = int(input())
    ls = list(map(int, input().split()))

    ls.sort()
    L=0

    for j in ls:
        if j > L:
            L+=1

    print(f'case #{t+1}: {L}')

T=int(input())
for i in range(T):
    solve(i)