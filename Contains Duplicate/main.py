class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        after_arranging = set(nums)

        if(len(nums) == len(after_arranging)):
            return False

        else:
            return True 
            
                     
        