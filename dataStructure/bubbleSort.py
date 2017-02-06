# 冒泡排序 二层循环格式
def bubblesort(A):
    n = len(A)
    for i in range(n,1,-1): # i = n, n-1, n-2, ..., 2
        print("")
        for j in range(n):
            print(str(A[j]), " ", end="")
        print(" ")
        # 截取 A 的前i个元素进行冒泡
        for j in range(i-1):
            if A[j] < A[j+1]:   # 依次比较两个相邻的数
                A[j], A[j+1] = A[j+1], A[j]     #交换两个相邻的数
            print("i=", str(i), " A[", str(j), "]= ", str(A[j]) , " A[", str(j+1), "]= ", str(A[j+1]))
