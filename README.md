# DSA
#2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        
        for i, x in enumerate(nums):
            if x == target:
                res.append(i)
        
        return res
