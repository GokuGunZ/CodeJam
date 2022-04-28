t = int(input()) # read a line with a single integer

pank = []

for i in range(0, t):
    l = int(input())
    dotti = []
    dotti= [int(s) for s in input().split(" ")]
    pank.append(dotti)

for i in range(len(pank)):
    ncustomer = 0
    if pank[i][0] < pank[i][-1] :
        mini=pank[i][0]
    else:
        mini=pank[i][-1]
    for j in range(len(pank[i])):
        if pank[i][0]<pank[i][-1]:
            if pank[i][0]>=mini:
                ncustomer+=1
                mini=pank[i][0]
            pank[i].pop(0)
        else :
            if pank[i][-1]>=mini:
                mini=pank[i][-1]
                ncustomer+=1
            pank[i].pop(-1)
    print(f'Case #{i+1}: {ncustomer}')