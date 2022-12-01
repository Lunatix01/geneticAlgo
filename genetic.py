import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
# colors, color bits and color representation
colorz = ['red', 'green', 'purple', 'orange']
colorBits = ['00', '01', '10', '11']
colorRep = ['0.1', '0.2', '0.3', '0.4']

# create generation 1 of random population


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
    return dataInBits


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


sample1 = checkboard(8)
sample2 = checkboard(8)
sample3 = checkboard(8)
sample4 = checkboard(8)
sample5 = checkboard(8)
sample6 = checkboard(8)
sample7 = checkboard(8)
sample8 = checkboard(8)
sample9 = checkboard(8)
sample10 = checkboard(8)

listOfFirstGen = [sample1, sample2, sample3, sample4,
                  sample5, sample6, sample7, sample8, sample9, sample10]

fitnesses = [fitness(sample1), fitness(sample2), fitness(sample3), fitness(sample4),
             fitness(sample5), fitness(sample6), fitness(sample7), fitness(sample8), fitness(sample9), fitness(sample10)]
listOfFirstGenFit = [fitness(sample1), fitness(sample2), fitness(sample3), fitness(sample4), fitness(sample5),
                     fitness(sample6), fitness(sample7), fitness(sample8), fitness(sample9), fitness(sample10)]

# listOfRandomChoices.sort()
# print(listOfRandomChoices)
print(fitnesses)
# print(sorted(fitnesses)[9])

sorttedFitness = sorted((e, i) for i, e in enumerate(fitnesses))
print(sorttedFitness, 'sorted fitness')
# multiply by 1 to start of list for second multiply by 10, for third multiply by 100 so on
count = 5
sorttedFitnessOfWithMargin = sorttedFitness.copy()
for i in range(10):
    sorttedFitnessOfWithMargin[i] = (
        sorttedFitness[i][0]*count, sorttedFitness[i][1])
    count += 5
print(sorttedFitnessOfWithMargin, 'sorttedFitnessOfWithMargin')

listOfUpdatedFitness = []
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    listOfUpdatedFitness.append(sorttedFitnessOfWithMargin[i][0])
    labels[i] = sorttedFitnessOfWithMargin[i][1]
print(listOfUpdatedFitness, 'updated fitness')
print(labels, 'labels')
listOfRandomChoices = random.choices(
    labels, weights=listOfUpdatedFitness, k=10)
print(listOfRandomChoices, 'random choices')
first = np.random.choice(listOfRandomChoices, size=10, replace=False)


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


first = split(first, 2)

# loop to check if each array inside first array are the same if yes then regenerate
for i in range(5):
    if first[i][0] == first[i][1]:
        first = np.random.choice(
            listOfRandomChoices, size=10, replace=False)
        first = split(first, 2)
        break
    else:
        pass


def crossover(data, data2):
    leng = len(data)
    temp = np.copy(data)
    temp2 = np.copy(data2)

    for i in range(leng):
        randomList = np.arange(i, leng).tolist()

        indexes = np.random.choice(
            randomList, size=int(np.fix((leng-i)/2)), replace=False)
        for j in indexes:
            temp[i, j] = data2[j, i]
            temp2[j, i] = data[i, j]

    return temp, temp2


print("indexes of first", first[0][0], first[0][1])
sample1, sample2 = crossover(
    listOfFirstGen[first[0][0]], listOfFirstGen[first[0][1]])
sample3, sample4 = crossover(
    listOfFirstGen[first[1][0]], listOfFirstGen[first[1][1]])
sample5, sample6 = crossover(
    listOfFirstGen[first[2][0]], listOfFirstGen[first[2][1]])
sample7, sample8 = crossover(
    listOfFirstGen[first[3][0]], listOfFirstGen[first[3][1]])
sample9, sample10 = crossover(
    listOfFirstGen[first[4][0]], listOfFirstGen[first[4][1]])
fitnesses = [fitness(sample1), fitness(sample2), fitness(sample3), fitness(sample4),
             fitness(sample5), fitness(sample6), fitness(sample7), fitness(sample8), fitness(sample9), fitness(sample10)]

print('------------------------1')
print(listOfFirstGen[first[0][0]], 'sample1')
print('------------------------')
print(sample1, 'afterCrossover1')
print('------------------------1')
print(listOfFirstGen[first[0][1]], 'sample2')
print('------------------------1')
print(sample2, 'afterCrossover2')
print('------------------------')


# def checkDuplicates(listOfRandomChoices, first, second, third, fourth, fifth):
#     isThereDuplicates = True
#     while isThereDuplicates:
#         if first[0] == first[1]:
#             first = np.random.choice(
#                 listOfRandomChoices, size=2, replace=False)
#         elif second[0] == second[1]:
#             second = np.random.choice(
#                 listOfRandomChoices, size=2, replace=False)
#         elif third[0] == third[1]:
#             third = np.random.choice(
#                 listOfRandomChoices, size=2, replace=False)
#         elif fourth[0] == fourth[1]:
#             fourth = np.random.choice(
#                 listOfRandomChoices, size=2, replace=False)
#         elif fifth[0] == fifth[1]:
#             fifth = np.random.choice(
#                 listOfRandomChoices, size=2, replace=False)
#         else:
#             isThereDuplicates = False
#     return first, second, third, fourth, fifth


# first, second, third, fourth, fifth = checkDuplicates(
#     listOfRandomChoices, first, second, third, fourth, fifth)


# isThereSimilar = True
# arrayOfPairs = [first, second, third, fourth, fifth]
# print(arrayOfPairs, 'array of pairs')
# setOfChoices = set(set(tuple(i) for i in arrayOfPairs))
# print(len(setOfChoices), 'length of set')

# print(setOfChoices, 'set of choices')


# fitness function


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


# afterCross = {
#     1: dataAfterCross,
#     2: dataAfterCross2,
#     3: dataAfterCross3,
#     4: dataAfterCross4,
#     5: dataAfterCross5,
#     6: dataAfterCross6,
#     7: dataAfterCross7,
#     8: dataAfterCross8,
#     9: dataAfterCross9,
#     10: dataAfterCross10
# }

#  mutation function


def mutation(data):
    for i in range(len(data)):
        # indexes = np.random.choice(len(data), size=4, replace=False)
        bits = np.random.choice(
            ['00', '01', '10', '11'], size=4, replace=False)
        oddOrEven = np.random.choice([0, 1], size=1, replace=False)
        if (oddOrEven == 0 and i % 2 == 0):
            data[i, 0] = bits[0]
            data[i, 2] = bits[1]
            data[i, 4] = bits[2]
            data[i, 6] = bits[3]
        else:
            data[i, 1] = bits[0]
            data[i, 3] = bits[1]
            data[i, 5] = bits[2]
            data[i, 7] = bits[3]
    return data


def checkAnswer(listOfFitness):
    # iterate through bestFit and check if close to answer %90 of 256
    for i in range(len(listOfFitness)):
        if (listOfFitness[i] == 256):
            return True, i
    return False, -1


checked, i = checkAnswer(fitnesses)
loopthrough = False
loopcount = 0
bestofbest = 0
bestofbestBoard = np.zeros((8, 8))
lastBest = 0
# get 5 old best generation
while (loopthrough == False):
    np.random.seed(loopcount)
    listOfFirstGen = [sample1, sample2, sample3, sample4,
                      sample5, sample6, sample7, sample8, sample9, sample10]
    fitnesses = [fitness(sample1), fitness(sample2), fitness(sample3), fitness(sample4),
                 fitness(sample5), fitness(sample6), fitness(sample7), fitness(sample8), fitness(sample9), fitness(sample10)]
    sorttedFitness = sorted((e, i) for i, e in enumerate(fitnesses))
    count = 5
    sorttedFitnessOfWithMargin = sorttedFitness.copy()
    for i in range(10):
        sorttedFitnessOfWithMargin[i] = (
            sorttedFitness[i][0]*count, sorttedFitness[i][1])
        count += 5
    listOfUpdatedFitness = []
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(10):
        listOfUpdatedFitness.append(sorttedFitnessOfWithMargin[i][0])
        labels[i] = sorttedFitnessOfWithMargin[i][1]
    listOfRandomChoices = random.choices(
        labels, weights=listOfUpdatedFitness, k=10)
    first = np.random.choice(listOfRandomChoices, size=10, replace=False)
    first = split(first, 2)
    # loop to check if each array inside first array are the same if yes then regenerate
    for i in range(5):
        if first[i][0] == first[i][1]:
            first = np.random.choice(
                listOfRandomChoices, size=10, replace=False)
            first = split(first, 2)
            break
        else:
            pass
    sample1, sample2 = crossover(
        listOfFirstGen[first[0][0]], listOfFirstGen[first[0][1]])
    sample3, sample4 = crossover(
        listOfFirstGen[first[1][0]], listOfFirstGen[first[1][1]])
    sample5, sample6 = crossover(
        listOfFirstGen[first[2][0]], listOfFirstGen[first[2][1]])
    sample7, sample8 = crossover(
        listOfFirstGen[first[3][0]], listOfFirstGen[first[3][1]])
    sample9, sample10 = crossover(
        listOfFirstGen[first[4][0]], listOfFirstGen[first[4][1]])
    listOfFirstGen = [sample1, sample2, sample3, sample4,
                      sample5, sample6, sample7, sample8, sample9, sample10]
    fitnesses = [fitness(sample1), fitness(sample2), fitness(sample3), fitness(sample4),
                 fitness(sample5), fitness(sample6), fitness(sample7), fitness(sample8), fitness(sample9), fitness(sample10)]
    checked, i = checkAnswer(fitnesses)

    if (checked == True):
        print("found answer in generation", fitnesses)
        bestofbest = fitnesses[i]
        bestofbestBoard = listOfFirstGen[i]
        loopthrough = True
        break
    if (max(fitnesses) > bestofbest):
        bestofbest = max(fitnesses)
        max_index = fitnesses.index(max(fitnesses))
        bestofbestBoard = listOfFirstGen[max_index]
        lastBest = loopcount
    if (loopcount == lastBest+25):
        print('mutate', lastBest)
        sample1 = mutation(sample1)
        sample2 = mutation(sample2)
        sample3 = mutation(sample3)
        sample4 = mutation(sample4)
        sample5 = mutation(sample5)
        sample6 = mutation(sample6)
        sample7 = mutation(sample7)
        sample8 = mutation(sample8)
        sample9 = mutation(sample9)
        sample10 = mutation(sample10)

    loopcount += 1
    if (loopcount == 100):
        loopthrough = True
    # else:
    #     loopthrough = True
    #     print("close to answer")
    #     print(checked)
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

plt.title("fitness: "+str(bestofbest))
plt.show()
