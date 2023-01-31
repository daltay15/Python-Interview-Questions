
# Problem: Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
# Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

s = "ABAB"
k = 2


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}  # Initialize hashmap
        res = 0
        l = 0
        for r in range(len(s)): # Loop the right pointer through range of numbers opening the window
            count[s[r]] = 1 + count.get(s[r], 0)    # Increment count at current position

            while (r - l + 1) - max(count.values()) > k:    # While window ! valid - count of most freq character 
                count[s[1]] -= 1    # Decrement count of character at left positon and decrement by 1
                l += 1  # move left pointer right by 1

            res = max(res, r - l + 1)   # set res to max of current res and size of window
        
        return res


if __name__ == "__main__":
    print(Solution().characterReplacement(s, k))