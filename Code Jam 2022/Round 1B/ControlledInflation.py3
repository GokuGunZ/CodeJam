t = int(input()) # read a line with a single integer
products = []
finalresult = 0



for i in range(0, t):
    costumers, prod = [int(s) for s in input().split(" ")]
    pitucci=[]
    for j in range(costumers):
        dotti= [int(s) for s in input().split(" ")]
        dotti.sort()
        pitucci.append(dotti)
        
    products.append(pitucci)

for i in range(len(products)):
    finalresult+=products[i][0][-1]
    pressAtt = products[i][0][-1]
    for j in range(1, len(products[i])):
        distDx = abs(products[i][j][-1]-pressAtt)
        distSx = abs(products[i][j][0]-pressAtt)
        if distDx==distSx and j<len(products[i]) :
            distDD = abs(products[i][j+1][-1]-products[i][j][-1])
            distSD = abs(products[i][j+1][0]-products[i][j][-1])
            distDS = abs(products[i][j+1][-1]-products[i][j][0])
            distSS = abs(products[i][j+1][0]-products[i][j][0])
            if min(distSS, distSD, distDS, distDD) == min(distDD, distDS):
                finalresult+=distSx
                finalresult+=products[i][j][-1]-products[i][j][0]
                pressAtt = products[i][j][-1]
            else: 
                finalresult+=distDx
                finalresult+=products[i][j][-1]-products[i][j][0]
                pressAtt = products[i][j][0]
        elif distDx<distSx:
            finalresult+=distDx
            finalresult+=products[i][j][-1]-products[i][j][0]
            pressAtt = products[i][j][0]
        else:
            finalresult+=distSx
            finalresult+=products[i][j][-1]-products[i][j][0]
            pressAtt = products[i][j][-1]
        
    print(f'Case #{i+1}: {finalresult}')
    finalresult=0
    