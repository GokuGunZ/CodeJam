printer1 = []
printer2 = []
printer3 = []

t=int(input())
results=[]
for i in range(1, t + 1):
    c, m, y, k = [int(s) for s in input().split(" ")]
    printer1.append([c, m, y, k])
    c, m, y, k = [int(s) for s in input().split(" ")]
    printer2.append([c, m, y, k])
    c, m, y, k = [int(s) for s in input().split(" ")]
    printer3.append([c, m, y, k])

    
for i in range(t):
    min_c=min(printer1[i][0], printer2[i][0], printer3[i][0])
    min_m=min(printer1[i][1], printer2[i][1], printer3[i][1])
    min_y=min(printer1[i][2], printer2[i][2], printer3[i][2])
    min_k=min(printer1[i][3], printer2[i][3], printer3[i][3])
    summin=min_c+min_m+min_y+min_k
    if summin<1000000:
        results.append('IMPOSSIBLE')
        continue
    if min_c>1000000:
        results.append('1000000 0 0 0')
        continue
    if (min_c+min_m)>1000000:
        rest=1000000-min_c
        results.append('{} {} 0 0'.format(min_c, rest))
        continue
    if (min_c+min_m+min_y)>1000000:
        rest=1000000-min_c-min_m
        results.append('{} {} {} 0'.format(min_c, min_m, rest))
        continue 
    rest=1000000-min_c-min_m-min_y

    results.append('{} {} {} {}'.format(min_c, min_m, min_y, rest))

for i in range(t):
    print('Case #{}: {}'.format(i+1, results[i]))
    