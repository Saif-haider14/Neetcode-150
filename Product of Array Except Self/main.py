# Brutal Force Technique 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        
        for i in range(len(nums)):
            
            n = 1
            temp = nums[:i] + nums[i+1:]
            for j in temp:
                
                n = n*j
            output.append(n)
        return output 
            