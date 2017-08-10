'''
Created on 2012-11-9

@author: Pandara
'''

def lcs_len(strRowAlphas, strColumnAlphas):
    '''
    a, b: strings
    '''
    rows = len(strRowAlphas)
    cols = len(strColumnAlphas)

    length = [([0] * (cols + 1)) for i in range(rows + 1)]
    direct = [([0] * cols) for i in range(rows)]  # 0 for top left, -1 for left, 1 for top

    for row in range(rows + 1)[1:]:
        for col in range(cols + 1)[1:]:
            if strRowAlphas[row - 1] == strColumnAlphas[col - 1]:
                length[row][col] = length[row - 1][col - 1] + 1 #↖(左斜角) 默认的0
            elif length[row][col - 1] > length[row - 1][col]:
                length[row][col] = length[row][col - 1]
                direct[row - 1][col - 1] = -1 #←（左侧）-1
            else:
                length[row][col] = length[row - 1][col]
                direct[row - 1][col - 1] = 1 #↑（上面） 1

    return length, direct


def get_lcs(direct, a, i, j):
    '''
    direct: martix of arrows
    a: the string regarded as row
    i: len(a) - 1, for initialization
    j: len(b) - 1, for initialization
    '''
    lcs = []
    get_lcs_inner(direct, a, i, j, lcs)
    return lcs


def get_lcs_inner(direct, a, i, j, lcs):
    if i < 0 or j < 0:
        return

    if direct[i][j] == 0:
        get_lcs_inner(direct, a, i - 1, j - 1, lcs)
        lcs.append(a[i])

    elif direct[i][j] == 1:
        get_lcs_inner(direct, a, i - 1, j, lcs)
    else:
        get_lcs_inner(direct, a, i, j - 1, lcs)


if __name__ == "__main__":
    a = "ABCBDAB"
    b = "BDCABA"

    length, direct = lcs_len(a, b)
    lcs = get_lcs(direct, a, len(a) - 1, len(b) - 1)

    print("the length of lcs is:", length[len(a)][len(b)])
    print("one of the lcs:", "".join(lcs))
