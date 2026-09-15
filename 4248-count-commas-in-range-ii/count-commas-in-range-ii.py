class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        power = 3
        while power <=15:
            diff = n - 10**power +1
            if diff >0:
                res += diff
            power+=3
        return res
        