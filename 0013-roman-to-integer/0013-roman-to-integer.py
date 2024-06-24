class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        result = 0
        index = 0

        while index <= len(s) - 1:
            if index != len(s) - 1 and dict[s[index]] < dict[s[index+1]]:
                result += dict[s[index] + s[index + 1]]
                index += 2
            else:
                result += dict[s[index]]
                index += 1

        return result