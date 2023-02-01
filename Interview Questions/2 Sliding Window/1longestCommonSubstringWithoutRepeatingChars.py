# Problem: Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # Create a set to store the characters
        result = 0  # Initialize the result

        left = 0    # Initialize the left pointer

        for right in range(len(s)): # Iterate through the string
            while s[right] in charSet:  # While the character is in the set
                charSet.remove(s[left]) # Remove the character from the set
                left += 1   # Increment the left pointer
            charSet.add(s[right])   # Add the character to the set
            result = max(result, right - left + 1)  # Update the result
        return result
        

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))