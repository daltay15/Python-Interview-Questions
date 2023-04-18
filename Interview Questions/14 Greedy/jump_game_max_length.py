# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

class Solution:
    def exitArrayMin(self, nums):
        if len(nums) == 1:
            return 0
        
        jumps = 0 # initialize the number of jumps to 0
        current_jump_end = 0 # initialize the current jump end to 0
        farthest = 0 # initialize the farthest to 0
        
        for i in range(len(nums) - 1): # iterate from 0 to the length of the array - 1
            farthest = max(farthest, i + nums[i]) # set the farthest to the max of the farthest and the current index + the value at the current index
            if i == current_jump_end: # if the current index is equal to the current jump end
                jumps += 1 # increment the number of jumps by 1
                current_jump_end = farthest # set the current jump end to the farthest
        return jumps 
    

if __name__ == "__main__":
    nums = [1,2,5,2,1,1]
    print(Solution().exitArrayMin(nums))