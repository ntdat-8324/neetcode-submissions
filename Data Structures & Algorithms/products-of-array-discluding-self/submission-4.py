class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        n = len(nums)
        prefix = [1] * n
        suff = [1] * (n + 1)
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 1, 0, -1):
            suff[i] = suff[i + 1] * nums[i]
        outputs = [prefix[i - 1] * suff[i + 1] for i in range(1, n)]
        return outputs
        