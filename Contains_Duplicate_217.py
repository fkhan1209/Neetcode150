class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums) #finds the length of the original list of numbers 
        nums_set = set(nums) #instatiates a set of the numbers list -- removing all duplicates
        set_length = len (nums_set) #finds the length of the set of numbers  
        if length == set_length: 
            return False 
        else:
            return True #if condition checking for lengths of both the set and list of numbers