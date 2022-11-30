import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# colors, color bits and color representation
colorz = ['red', 'green', 'purple', 'orange']
colorBits = ['00', '01', '10', '11']
colorRep = ['0.1', '0.2', '0.3', '0.4']

# create generation 0 of random population


def checkboard(n):
    dataz = np.random.choice(colorz, size=(n, n))
    datas = np.random.rand(n, n)
    dataInBits = np.random.choice(colorz, size=(n, n))
    for i in range(n):
        for j in range(n):
            if dataz[i, j] == 'red':
                datas[i, j] = 0.1
                dataInBits[i, j] = '00'
            elif dataz[i, j] == 'green':
                datas[i, j] = 0.2
                dataInBits[i, j] = '01'
            elif dataz[i, j] == 'purple':
                datas[i, j] = 0.3
                dataInBits[i, j] = '10'
            elif dataz[i, j] == 'orange':
                datas[i, j] = 0.4
                dataInBits[i, j] = '11'
    return datas, dataz, dataInBits


data, dataz, dataInBits = checkboard(8)
data2, dataz2, dataInBits2 = checkboard(8)
data3, dataz3, dataInBits3 = checkboard(8)
data4, dataz4, dataInBits4 = checkboard(8)
data5, dataz5, dataInBits5 = checkboard(8)
data6, dataz6, dataInBits6 = checkboard(8)
data7, dataz7, dataInBits7 = checkboard(8)
data8, dataz8, dataInBits8 = checkboard(8)
data9, dataz9, dataInBits9 = checkboard(8)
data10, dataz10, dataInBits10 = checkboard(8)


# crossover function


# def crossover(data, data2):
#     leng = len(data)
#     temp = data.copy()
#     temp2 = data2.copy()
#     for i in range(leng):
#         for j in range(leng):
#             if j >= 4:
#                 data[i, j] = temp2[i, j]
#                 data2[i, j] = temp[i, j]
#     return data, data2
def crossover(data, data2):
    leng = len(data)
    temp = data.copy()
    temp2 = data2.copy()
    for i in range(leng):
        for j in range(leng):
            if j >= 4:
                data[i, j] = temp2[i, j]
                data2[i, j] = temp[i, j]
    return data, data2


dataAfterCross, dataAfterCross2 = crossover(dataInBits, dataInBits2)
dataAfterCross3, dataAfterCross4 = crossover(dataInBits3, dataInBits4)
dataAfterCross5, dataAfterCross6 = crossover(dataInBits5, dataInBits6)
dataAfterCross7, dataAfterCross8 = crossover(dataInBits7, dataInBits8)
dataAfterCross9, dataAfterCross10 = crossover(dataInBits9, dataInBits10)

afterCross = {
    1: dataAfterCross,
    2: dataAfterCross2,
    3: dataAfterCross3,
    4: dataAfterCross4,
    5: dataAfterCross5,
    6: dataAfterCross6,
    7: dataAfterCross7,
    8: dataAfterCross8,
    9: dataAfterCross9,
    10: dataAfterCross10
}

# mutation function


def mutation(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i, j] == '00':
                data[i, j] = '11'
            elif data[i, j] == '11':
                data[i, j] = '00'
    return data

# fitness function


def fitness(data):
    fit = 0
    leng = len(data)
    for i in range(leng):
        for j in range(leng):
            point = data[i, j]
            if j != leng-1 and point != data[i, j+1]:
                fit += 1
            if i != leng-1 and point != data[i+1, j]:
                fit += 1
            if j != 0 and point != data[i, j-1]:
                fit += 1
            if i != 0 and point != data[i-1, j]:
                fit += 1
            if i == 0:
                fit += 1
            if i == leng-1:
                fit += 1
            if j == 0:
                fit += 1
            if j == leng-1:
                fit += 1

    return fit


fit = fitness(dataAfterCross)
# print(fit)
# print(dataAfterCross)
fit2 = fitness(dataAfterCross2)
fit3 = fitness(dataAfterCross3)
fit4 = fitness(dataAfterCross4)
fit5 = fitness(dataAfterCross5)
fit6 = fitness(dataAfterCross6)
fit7 = fitness(dataAfterCross7)
fit8 = fitness(dataAfterCross8)
fit9 = fitness(dataAfterCross9)
fit10 = fitness(dataAfterCross10)
print("fit1", fit, "fit2", fit2, "fit3", fit3, "fit4", fit4, "fit5", fit5,
      "fit6", fit6, "fit7", fit7, "fit8", fit8, "fit9", fit9, "fit10", fit10)

# get 5 best fitness key and value key is equal to number of generation and value is equal to fitness


def getBestFit(fit, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10):
    bestFit = {1: fit, 2: fit2, 3: fit3, 4: fit4, 5: fit5,
               6: fit6, 7: fit7, 8: fit8, 9: fit9, 10: fit10}
    bestFit = sorted(bestFit.items(), key=lambda x: x[1])
    bestFit = bestFit[5:]
    return bestFit


bestFit = getBestFit(fit, fit2, fit3, fit4, fit5,
                     fit6, fit7, fit8, fit9, fit10)
afterCross = {
    1: afterCross[bestFit[0][0]],
    2: afterCross[bestFit[1][0]],
    3: afterCross[bestFit[2][0]],
    4: afterCross[bestFit[3][0]],
    5: afterCross[bestFit[4][0]]
}
# print("bestFit", bestFit)
# check if close to answer 8*8 in max= 8*8*4= 256 fitness


def checkAnswer(bestFit):
    # iterate through bestFit and check if close to answer %90 of 256
    for i in range(len(bestFit)):
        if bestFit[i][1] >= 256*0.99:
            return bestFit[i][1]
    return False


checked = checkAnswer(bestFit)
newCross = {}
loopthrough = False
loopcount = 0
bestofbest = 0
bestofbestBoard = np.zeros((8, 8))
bestInEachGen = []
lastBest = 0
# get 5 old best generation
while (loopthrough == False):
    # oldCross = {}
    # for i in range(len(bestFit)):
    #     oldCross[i] = afterCross[bestFit[i][0]]
    # generate 10 generations
    data, dataz, dataInBits = checkboard(8)
    data2, dataz2, dataInBits2 = checkboard(8)
    data3, dataz3, dataInBits3 = checkboard(8)
    data4, dataz4, dataInBits4 = checkboard(8)
    data5, dataz5, dataInBits5 = checkboard(8)
    data6, dataz6, dataInBits6 = checkboard(8)
    data7, dataz7, dataInBits7 = checkboard(8)
    data8, dataz8, dataInBits8 = checkboard(8)
    data9, dataz9, dataInBits9 = checkboard(8)
    data10, dataz10, dataInBits10 = checkboard(8)
    # crossover function
    dataAfterCross, dataAfterCross2 = crossover(dataInBits, dataInBits2)
    dataAfterCross3, dataAfterCross4 = crossover(dataInBits3, dataInBits4)
    dataAfterCross5, dataAfterCross6 = crossover(dataInBits5, dataInBits6)
    dataAfterCross7, dataAfterCross8 = crossover(dataInBits7, dataInBits8)
    dataAfterCross9, dataAfterCross10 = crossover(
        dataInBits9, dataInBits10)

    afterCross2 = {
        1: dataAfterCross,
        2: dataAfterCross2,
        3: dataAfterCross3,
        4: dataAfterCross4,
        5: dataAfterCross5,
        6: dataAfterCross6,
        7: dataAfterCross7,
        8: dataAfterCross8,
        9: dataAfterCross9,
        10: dataAfterCross10
    }

    fit = fitness(dataAfterCross)
    fit2 = fitness(dataAfterCross2)
    fit3 = fitness(dataAfterCross3)
    fit4 = fitness(dataAfterCross4)
    fit5 = fitness(dataAfterCross5)
    fit6 = fitness(dataAfterCross6)
    fit7 = fitness(dataAfterCross7)
    fit8 = fitness(dataAfterCross8)
    fit9 = fitness(dataAfterCross9)
    fit10 = fitness(dataAfterCross10)
    bestFit2 = getBestFit(fit, fit2, fit3, fit4, fit5,
                          fit6, fit7, fit8, fit9, fit10)
    checked = checkAnswer(bestFit)
    # print("bestFit2", bestFit2)
    afterCross2 = {
        1: afterCross2[bestFit2[0][0]],
        2: afterCross2[bestFit2[1][0]],
        3: afterCross2[bestFit2[2][0]],
        4: afterCross2[bestFit2[3][0]],
        5: afterCross2[bestFit2[4][0]]
    }
    # print(bestFit)
    if (checked == False):
        dataAfterCross, dataAfterCross2 = crossover(
            afterCross[1], afterCross2[1])
        dataAfterCross3, dataAfterCross4 = crossover(
            afterCross[2], afterCross2[2])
        dataAfterCross5, dataAfterCross6 = crossover(
            afterCross[3], afterCross2[3])
        dataAfterCross7, dataAfterCross8 = crossover(
            afterCross[4], afterCross2[4])
        dataAfterCross9, dataAfterCross10 = crossover(
            afterCross[5], afterCross2[5])

        # if (loopcount-lastBest > 100):
        #     lastBest = 0
        #     dataAfterCross = mutation(dataAfterCross)
        #     dataAfterCross2 = mutation(dataAfterCross2)
        #     dataAfterCross3 = mutation(dataAfterCross3)
        #     dataAfterCross4 = mutation(dataAfterCross4)
        #     dataAfterCross5 = mutation(dataAfterCross5)
        #     dataAfterCross6 = mutation(dataAfterCross6)
        #     dataAfterCross7 = mutation(dataAfterCross7)
        #     dataAfterCross8 = mutation(dataAfterCross8)
        #     dataAfterCross9 = mutation(dataAfterCross9)
        #     dataAfterCross10 = mutation(dataAfterCross10)
        afterCross = {
            1: dataAfterCross,
            2: dataAfterCross2,
            3: dataAfterCross3,
            4: dataAfterCross4,
            5: dataAfterCross5,
            6: dataAfterCross6,
            7: dataAfterCross7,
            8: dataAfterCross8,
            9: dataAfterCross9,
            10: dataAfterCross10
        }
        fit = fitness(dataAfterCross)
        fit2 = fitness(dataAfterCross2)
        fit3 = fitness(dataAfterCross3)
        fit4 = fitness(dataAfterCross4)
        fit5 = fitness(dataAfterCross5)
        fit6 = fitness(dataAfterCross6)
        fit7 = fitness(dataAfterCross7)
        fit8 = fitness(dataAfterCross8)
        fit9 = fitness(dataAfterCross9)
        fit10 = fitness(dataAfterCross10)
        bestFit = getBestFit(fit, fit2, fit3, fit4, fit5,
                             fit6, fit7, fit8, fit9, fit10)
        # print("bestFit", bestFit)
        afterCross = {
            1: afterCross[bestFit[0][0]],
            2: afterCross[bestFit[1][0]],
            3: afterCross[bestFit[2][0]],
            4: afterCross[bestFit[3][0]],
            5: afterCross[bestFit[4][0]]
        }
        if (bestFit[4][1] > bestofbest):
            bestofbest = bestFit[4][1]
            bestInEachGen.append(bestofbest)
            bestofbestBoard = afterCross[5].copy()
            lastBest = loopcount
            print("bestofbestBoard", bestofbestBoard)
            print("bestofbest", bestofbest)
            print("loop", loopcount)
        if (bestFit[4][1] == 256):
            print("found answer")
            print(afterCross[bestFit[4][0]])
            print(bestFit[4][1])
            break
        loopcount += 1
        if (loopcount == 1000000):
            loopthrough = True
    else:
        loopthrough = True
        print("close to answer")
        print(checked)
print("best of best", bestofbest)
print("best of best board", bestofbestBoard)
showboard = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        if bestofbestBoard[i, j] == '00':
            showboard[i, j] = 0.1
        elif bestofbestBoard[i, j] == '01':
            showboard[i, j] = 0.2
        elif bestofbestBoard[i, j] == '10':
            showboard[i, j] = 0.3
        elif bestofbestBoard[i, j] == '11':
            showboard[i, j] = 0.4

col = colors.ListedColormap(colorz)
fig, ax = plt.subplots()
im = ax.imshow(showboard, cmap=col)
# print(bestInEachGen)
# plt.hist(bestInEachGen)

plt.show()
