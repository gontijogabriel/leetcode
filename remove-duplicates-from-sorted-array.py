"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    res = []

    for n in nums:
        if len(res) == 0:
            res.append(n)
        else:
            if n not in res:
                res.append(n)
            

    return res

print(removeDuplicates([1,1,2]))