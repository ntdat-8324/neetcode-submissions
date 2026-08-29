class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0 , len(numbers)-1
        
        # -4 -3 -1 3 4 8 | 3

        while i < j:
            
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            
            if sum < target:
                i += 1

            if sum > target:
                j -= 1