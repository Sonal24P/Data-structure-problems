"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:  
            return nums.index(target) #return the index of the target if present in list
        else:
            position =0
            if target>nums[-1]:
                return len(nums) # add in the end if target is the largest
            else:
                for index in range(len(nums)):
                    if target<nums[index]:
                        position =index
                        break
            return position # return the of the element if target is somwhere in the mid of the list
        