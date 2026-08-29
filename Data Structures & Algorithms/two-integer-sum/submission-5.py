class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     nums[i] = [i, nums[i]]
        
        # nums.sort(key=lambda item: item[1])
        # nums = [(val, idx) for idx, val in enumerate(nums)]
        # nums.sort()
        mp = {}
        for idx, val in enumerate(nums):
            need = target - val
            if need in mp:
                return [min(idx, mp[need]), max(idx, mp[need])]
            mp[val] = idx








        