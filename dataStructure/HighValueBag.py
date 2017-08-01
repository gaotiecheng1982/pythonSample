def HighValueBag(quantity, weightAmount, weight, value):
    resultTable = [[-1 for j in range(weightAmount + 1)] for i in range(quantity + 1)]

    for curWgt in range(weightAmount + 1):
        resultTable[0][curWgt] = 0
    print(repr(resultTable[0]))

    for i in range(1, quantity + 1):
        for curWgt in range(1, weightAmount + 1):
            resultTable[i][curWgt] = resultTable[i - 1][curWgt]
            if curWgt >= weight[i - 1] and resultTable[i][curWgt] < resultTable[i - 1][curWgt - weight[i - 1]] + value[i - 1]:  # 不装价值大
                resultTable[i][curWgt] = resultTable[i - 1][curWgt - weight[i - 1]] + value[i - 1]  # 前i-1个物品的最优解与第i个物品的价值之和更大
        print(repr(resultTable[i]))

    return resultTable


def Show(quantity, weightAmount, weight, resultTable):
    print('最大价值为:', resultTable[quantity][weightAmount])
    x = [False for i in range(quantity)]

    curWgt = weightAmount  #
    for i in range(quantity, 0, -1):
        if curWgt >= 0 and resultTable[i][curWgt] > resultTable[i - 1][curWgt]:
            x[i - 1] = True
            curWgt -= weight[i - 1]  # remove current thing

    print('选择的物品为:')
    for i in range(quantity):
        if x[i]:
            print('第', i, '个,', end='')


if __name__ == '__main__':
    quantity = 5  # things quantity
    weightAmount = 10  # weight amount
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    resultTable = HighValueBag(quantity, weightAmount, weight, value)
    Show(quantity, weightAmount, weight, resultTable)
