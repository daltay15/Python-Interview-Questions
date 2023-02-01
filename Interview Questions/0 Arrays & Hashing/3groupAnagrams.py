# Problem: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List
from collections import defaultdict



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimal m*n solution
        res = defaultdict(list) # Create a hashmap of lists

        for s in strs:  # Iterate through the list
            count = [0] * 26    # Create a hashmap of 26 0's to store the count of each letter

            for c in s: # Iterate through the string
                count[ord(c) - ord("a")] += 1   # subtract ascii value of current char from ascii of a to get position in hashmap
            
            res[tuple(count)].append(s) # Add the string to the hashmap at the position of the count
        return res.values() # Return the values of the hashmap

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
    