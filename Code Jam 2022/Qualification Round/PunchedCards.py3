t = int(input()) # read a line with a single integer
righe = []
colonne = []
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    righe.append(n)
    colonne.append(m)
for i in range(t):
    print('Case #{}:'.format(i+1))
    firstrow = '..' + (colonne[i]-1)*'+-'+'+'
    secondrow = '..' + (colonne[i]-1)*'|.'+'|'
    print(firstrow)
    print(secondrow)
    normrow1 = '+-'*(colonne[i]) + '+'
    normrow2 = '|.'*(colonne[i]) + '|'
    for j in range(righe[i]-1):
        print(normrow1)
        print(normrow2)
    print(normrow1)