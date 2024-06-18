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
        last_number = 0
        for x in s:
            number = roman[x]
            if len(numbers_list) > 0:
                if number > last_number:
                    r = number + (-1 * last_number)
                    numbers_list.append(r)
                else:
                    r = last_number + number
                    numbers_list.append(r)

            print(last_number)
            numbers_list.append(number)
            last_number = number

        print(numbers_list)
        print(sum(numbers_list))


result = Solution()
result.romanToInt(s = "LVIII")
result.romanToInt(s = "MCMXCIV")
