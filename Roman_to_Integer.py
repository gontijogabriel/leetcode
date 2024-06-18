class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        numbers_list = []
        for x in s:
            numbers_list.append(roman[x])

        
        numbers = []
        last = 0
        cont = 1
        for current in numbers_list:
            if cont == 1:
                numbers.append(current)
            
            if current <= last:
                numbers.append(current)

            if current > last:
                del(numbers[-1])
                numbers.append(current + (-1 * last))

            last = current
            cont += 1

        print(sum(numbers))
            


result = Solution()
result.romanToInt(s = "MCMXCIV")
result.romanToInt(s = "LVIII")
