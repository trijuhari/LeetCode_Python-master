class Solution:
    def twoSum(self, nums, target):
        num_visited = {}

        for i in  range(len(nums)):
            num = nums[i]
            complement =  target - num 

            if complement in num_visited:
                 return[i, num_visited[complement]]
            else:
                num_visited[num] = i 
                
