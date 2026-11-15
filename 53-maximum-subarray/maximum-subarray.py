class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0  #init since we will constantly update this

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub =  max(maxSub, curSum)
        
        return maxSub



        