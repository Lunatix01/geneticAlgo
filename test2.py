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
fit2 = fitness(dataAfterCross2)
fit3 = fitness(dataAfterCross3)
fit4 = fitness(dataAfterCross4)
fit5 = fitness(dataAfterCross5)
fit6 = fitness(dataAfterCross6)
fit7 = fitness(dataAfterCross7)
fit8 = fitness(dataAfterCross8)
fit9 = fitness(dataAfterCross9)
fit10 = fitness(dataAfterCross10)
dataAfterCross10 = np.array((['00', '11', '01', '00', '01', '11', '10', '11'],
                             ['01', '10', '11', '01', '11', '10', '01', '10'],
                             ['00', '11', '01', '11', '00', '01', '10', '11'],
                             ['10', '00', '10', '00', '01', '00', '11', '01'],
                             ['11', '10', '11', '01', '11', '00', '11', '10'],
                             ['10', '01', '00', '10', '01', '10', '11', '10'],
                             ['00', '10', '01', '00', '10', '11', '01', '00'],
                             ['10', '11', '01', '10', '01', '10', '10', '01']), dtype='<U2')
print(fit10)
showboard = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        if dataAfterCross10[i, j] == '00':
            showboard[i, j] = 0.1
        elif dataAfterCross10[i, j] == '01':
            showboard[i, j] = 0.2
        elif dataAfterCross10[i, j] == '10':
            showboard[i, j] = 0.3
        elif dataAfterCross10[i, j] == '11':
            showboard[i, j] = 0.4
col = colors.ListedColormap(colorz)
fig, ax = plt.subplots()
im = ax.imshow(showboard, cmap=col)
# print(bestInEachGen)
# plt.hist(bestInEachGen)

plt.show()
