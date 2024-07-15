class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            ('I', 1),
            ('IV', 4),
            ('V', 5),
            ('IX', 9),
            ('X', 10),
            ('XL', 40),
            ('L', 50),
            ('XC', 90),
            ('C', 100),
            ('CD', 400),
            ('D', 500),
            ('CM', 900),
            ('M', 1000)
        ]

        length = len(roman) - 1
        result = ''

        while length >= 0:
            if num < 0:
                break
            elif num < roman[length][1]:
                length -= 1
            elif num >= roman[length][1]:
                num -= roman[length][1]
                result += roman[length][0]

        return result