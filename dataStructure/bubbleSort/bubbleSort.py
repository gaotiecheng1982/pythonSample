#!/usr/bin/python3
# 冒泡排序 二层循环格式
def bubblesort(lst):
    n = len(lst)
    for i in range(n,1,-1): # i = n, n-1, n-2, ..., 2
        print("")
        for j in range(n):
            print(str(lst[j]), " ", end="")
        print(" ")
        # 截取 A 的前i个元素进行冒泡
        for j in range(i-1):
            if lst[j] < lst[j+1]:   # 依次比较两个相邻的数
                lst[j], lst[j + 1] = lst[j + 1], lst[j]     #交换两个相邻的数
            #print("i=", str(i), " A[", str(j), "]= ", str(A[j]) , " A[", str(j+1), "]= ", str(A[j+1]))
