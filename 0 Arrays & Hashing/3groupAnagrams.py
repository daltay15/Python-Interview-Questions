List = list
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimal m*n solution
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a-z

            for c in s:
                count[ord(c) - ord("a")] += 1   # subtract ascii value of current char from ascii of a to get position in hashmap
            
            res[tuple(count)].append(s)
        return res.values()

if __name__ == "__main__":
    print(Solution().groupAnagrams(strs))
    