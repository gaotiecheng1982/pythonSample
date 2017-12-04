
#!/usr/bin/python3
def insertSort(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]

        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp

    return lst
