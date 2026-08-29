class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=0
            freq[nums[i]]+=1

        for num, cnt in freq.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0: return res

        
        


        
