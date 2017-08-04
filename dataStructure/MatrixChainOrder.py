# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][]. 0th row and 0th
    # column of m[][] are not used
    m = [[1 for x in range(n)] for x in range(n)]

    # Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    # L is contained chain length.
    for cntChainLgth in range(2, n):
        for i in range(1, n - cntChainLgth +1):
            j = i + cntChainLgth - 1
            m[i][j] = sys.maxsize
            print('m[', i, '][', j, '] =', m[i][j], end='\n')
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    print('m[', i, '][', j, '] =', m[i][j], 'k=', k, end=' ')

    return m[1][n - 1]


if __name__ == '__main__':
    # 我们在这里并没有构建具体的矩阵，仅仅有一个一维数组来模拟矩阵的行列；四个矩阵就需要5个数字
    # 矩阵的分别为：A1[2][4];A2[4][5];A3[5][5];A4[5][3];
    # Driver program to test above function
    arr = [30, 35, 15, 5, 10, 20, 25]
    size = len(arr)
    print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, size)))
