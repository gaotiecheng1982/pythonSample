# 循环格式
from dataStructure.bubbleSort import bubblesort
from dataStructure.quickSort import quicksort

import string

#list = map(int, sys.argv[1:])  # Get all the arguments

list = [67, 78, 12, 35, 99, 16, 76]

#-------bubblesort -------------
#bubblesort(list)
#print(list)

# for i in range(0,6,1):
#     print(i)

#----------quickSort -----------
start = 0
end = len(list) - 1
quicksort(list, start, end)  # Sort the entire list of arguments


print(list)
