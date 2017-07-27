
def HighValueBag(quantity, c, w, v):
    resultTable = [[-1 for j in range(c + 1)] for i in range(quantity + 1)]

    for j in range(c + 1):
        resultTable[0][j] = 0
    print(repr(resultTable[0]))

    for i in range(1, quantity + 1):
        for j in range(1, c + 1):
            resultTable[i][j] = resultTable[i - 1][j]
            if j >= w[i - 1] and resultTable[i][j] < resultTable[i - 1][j - w[i - 1]] + v[i - 1]:
                resultTable[i][j] = resultTable[i - 1][j - w[i - 1]] + v[i - 1]
        print(repr(resultTable[i]))

    return resultTable

def Show(n, c, w, resultTable):
    print('最大价值为:', resultTable[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(1, n + 1):
        if resultTable[i][j] > resultTable[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print('第', i, '个,', end='')
    print('')

if __name__ == '__main__':
    quantity = 5 # things quantity
    weightAmount = 10 # weight amount
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    resultTable = HighValueBag(quantity, weightAmount, weight, value)
    Show(quantity, weightAmount, weight, resultTable)
