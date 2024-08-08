"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
# 1,2,4,1,3,4
# def mergeTwoLists(list1, list2):
#     pool = list1 + list2
#     res = []

#     for x in range(len(pool)):
#         a = min(pool)
#         res.append(a)
#         pool.remove(a)

#     return res

def mergeTwoLists(list1, list2):
    pool = []
    for x in list1:
        pool.append(x)
    for x in list2:
        pool.append(x)
        
    res = []

    for x in range(len(pool)):
        a = min(pool)
        res.append(a)
        pool.remove(a)

    return res
print(mergeTwoLists([1,2,4], [1,3,4]))