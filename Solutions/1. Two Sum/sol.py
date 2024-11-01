#O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} 
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in d:
                return [i , d[num2]]
            
            d[nums[i]] = i 