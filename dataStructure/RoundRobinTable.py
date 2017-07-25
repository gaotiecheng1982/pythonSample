# 将问题分成3大部分
# 第一部分为，根据已经填充的第一行，填写第二行
# 第二部分为，根据已经填充好的第一部分，填写第三四行
# 第三部分为，根据已经填充好的前四行，填写最后四行。

def GenernateRoundRobinTable(k, n, argArray):
    i = 1
    while i <= n:
        argArray[1][i] = i  # 设置日程表第一行
        i += 1
    print(repr(argArray[1]))

    m = 1  # 每次填充时，起始填充位置
    s = 1
    while s <= k: # 总问题规模子矩阵合并计算次数
        n //= 2  # 每次折半处理
        t = 1
        while t <= n:  # 子矩阵数目进行交叉赋值
            i = m + 1
            while i <= 2 * m:  # 按照行进行赋值，行内分组赋值，分组数目
                j = m + 1
                while j <= 2 * m:  # 每组内元素个数
                    argArray[i][j + (t - 1) * m * 2] = argArray[i - m][j + (t - 1) * m * 2 - m]  # 右下角等于左上角的值
                    argArray[i][j + (t - 1) * m * 2 - m] = argArray[i - m][j + (t - 1) * m * 2]  # 左下角等于右上角的值
                    j += 1
                print(repr(argArray[i]))
                i += 1
            t += 1
        m *= 2
        s += 1
    return


if __name__ == '__main__':
    # 总人数
    n = 8  # 总人数
    k = 3  # 2^k 阶数
    array = [([0] * (n + 1)) for i in range(n + 1)]
    GenernateRoundRobinTable(k, n, array)
