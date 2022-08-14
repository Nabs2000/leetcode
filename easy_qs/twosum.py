class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Go thru each number, and add it to the one after to check if it adds up
        # to target. If it doesn't then move on to the next one
        
        
        # for i in range(len(nums) - 1):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j + 1] == target:
        #             return [i, j + 1]
        
        ## WRONG CODE ABOVE: This was giving me index error because j + 1 can exceed the length
        
        ## 2nd attempt
        
        # Iterate thru the nums list
        # First element: iterate through the elements that are after it and see if element1 + element2 = target. If so, return the list of their indexes
        # Otherwise, go to the next element and iterate through elements after it and so on
        
        # This won't cause index error because there HAS to be a solution, per the question's disclaimer, so i will never equal len(nums) - 1
        
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]
        
