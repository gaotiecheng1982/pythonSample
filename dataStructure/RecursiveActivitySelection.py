"""The following implementation assumes that the activities
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a
single person, one at a time"""


# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that conatins finish time of all activities

def printMaxActivities(stTime, fnsTime):
    atvCount = len(fnsTime)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i)

    # Consider rest of the activities
    for j in range(atvCount):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if stTime[j] >= fnsTime[i]:
            print(j)
            i = j


def recursive_activity_selector(started, finished, result, i, j):
    if i >= j:
        return
    l = i + 1
    while l <= j:
        if started[l] >= finished[i] and finished[l] <= started[j]:
            result.append(l)
            break
        l += 1
    recursive_activity_selector(started, finished, result, l, j);


if __name__ == '__main__':
    # Driver program to test above function
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    printMaxActivities(s, f)

    result = []
    n = len(s) - 1
    i = 0
    recursive_activity_selector(s, f, result, i, n)
