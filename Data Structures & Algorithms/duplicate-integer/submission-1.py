class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        # for i in count.values():
        #     if i >1:
        #         return True
        # return False

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
