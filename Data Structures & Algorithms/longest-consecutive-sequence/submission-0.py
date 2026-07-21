class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        maxCount = 0
        for i in nums:
            while(i+1 in nums):
                count+=1
                i+=1
            maxCount = max(count,maxCount)
            count = 1
        return maxCount