class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)

        intervals.sort(key=lambda interval: interval[1])

        dp = [[(0,[]) for _ in range(5)] for _ in range(n)]
        dp[0][1]= (intervals[0][2], [intervals[0][3]])
        max_weight = intervals[0][2]

        for i in range(1,n):
            low,high,idx=0,i-1,-1

            while low <= high:
                mid = low + (high - low)//2
                if(intervals[mid][1]<intervals[i][0]):
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1

            for j in range(1,5):
                dp[i][j]=dp[i-1][j]
                if(idx!=-1):
                    new_weight = dp[idx][j-1][0] + intervals[i][2]
                    new_idx = dp[idx][j-1][1].copy()
                    new_idx.append(intervals[i][3])
                    new_idx.sort()

                    if dp[i][j][0] < new_weight or (dp[i][j][0] == new_weight and new_idx < dp[i][j][1]):
                        dp[i][j] = new_weight, new_idx
                
                if(j == 1):
                    single_weight = intervals[i][2]
                    single_idx = [intervals[i][3]]

                    if dp[i][j][0] < single_weight or (dp[i][j][0] == single_weight and single_idx < dp[i][j][1]):
                        dp[i][j] = (single_weight,single_idx)
                
                max_weight=max(max_weight,dp[i][j][0])
        
        res = [100000]
        for j in range(1,5):
            if max_weight == dp[n-1][j][0]:
                res = min(res, dp[n-1][j][1])

        return res


        