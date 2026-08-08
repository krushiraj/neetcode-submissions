class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        n = len(nums)
        expected_sum = n*(n+1)//2

        return expected_sum - sum