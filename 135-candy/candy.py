class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = n 
        i = 1

        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            highest = 0
            while i < n and ratings[i] > ratings[i-1]:
                highest += 1
                total += highest
                i += 1
            if i == n:
                return total

            lowest = 0 
            while i < n and ratings[i] < ratings[i-1]:
                lowest +=1
                total +=lowest
                i += 1

            total -= min(highest, lowest)

        return total
        