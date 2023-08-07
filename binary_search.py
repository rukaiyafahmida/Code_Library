import math


### Iterative
def binary_search_iter(target, arr):
    f = 0
    b = len(arr)-1

    while f<b:
        m = math.floor((f+b)/2)
        if arr[m]==target:
            return m+1
        if arr[m]<target:
            f = m+1
        elif arr[m]> target:
            b = m -1
    return "not found"



print(binary_search_iter(target=15, arr=[1,3,5,7,10,11]))
