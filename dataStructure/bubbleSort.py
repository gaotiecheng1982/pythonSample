# 冒泡排序 二层循环格式
def bubblesort(A):
    n = len(A)
    for i in range(n,1,-1): # i = n, n-1, n-2, ..., 2
        # 截取 A 的前i个元素进行冒泡
        for j in range(i-1):
            print(str(j) , " " ,str(A[j]))
            if A[j] < A[j+1]:   # 依次比较两个相邻的数
                A[j], A[j+1] = A[j+1], A[j]     #交换两个相邻的数

