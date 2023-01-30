import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        column_number = 0
        letters = string.ascii_uppercase

        for i, char in enumerate(columnTitle[::-1]):
            column_number += (letters.index(char) + 1) * (len(letters) ^ i)
            print(i, char, column_number)

        #column_number += letters.index(columnTitle[-1]) + 1

        return column_number



print(Solution().titleToNumber("A"))