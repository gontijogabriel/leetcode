"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    prim = []

    print(arr[0])
    for i in arr:
        for ii in arr[i]:
            print(ii)


    return


print(diagonalDifference(arr))