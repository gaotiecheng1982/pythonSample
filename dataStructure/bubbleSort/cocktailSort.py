def cocktail(lst):
    for i in range(len(lst) // 2):
        swap = False
        for j in range(1 + i, len(lst) - i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(lst) - i - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                swap = True
        if not swap:
            break
