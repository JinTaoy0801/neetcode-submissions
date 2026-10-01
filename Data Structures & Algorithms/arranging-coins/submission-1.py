class Solution:
    def arrangeCoins(self, n: int) -> int:
        temp = n

        i = 1
        while temp >= i:
            temp -= i
            i += 1
        return i - 1