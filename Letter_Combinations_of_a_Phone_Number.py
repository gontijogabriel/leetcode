from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = ['']

        for digit in digits:
            temp = []
            for r in res:
                for item in d[digit]:
                    temp.append(r + item) 
            res = temp 

        return res

a = Solution()
a.letterCombinations("23")