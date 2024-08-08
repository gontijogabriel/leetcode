"""
    https://leetcode.com/problems/length-of-last-word/
"""


def func(s: str) -> int:

    res = s.split()[-1:][0]
    
    return len(res)

print(func('luffy ainda é joyboy'))