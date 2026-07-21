class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCount = 0
        for i in nums:
            count = 1
            while(i+1 in nums):
                count+=1
                i+=1
            maxCount = max(count,maxCount)
        return maxCount