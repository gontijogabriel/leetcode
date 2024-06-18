from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first = strs[0]


        for others in strs[1:]:
            while not others.startswith(first):
                first = first[:-1]
                if not first:
                    return ""

        return print(first)


a = Solution()
a.longestCommonPrefix(["flower","flow","flight"])
a.longestCommonPrefix(["dog","racecar","car"])