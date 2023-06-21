class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #Instantiates new lists of elements in string 's' and string 't', returning the boolean value of whether or not the two lists are the same