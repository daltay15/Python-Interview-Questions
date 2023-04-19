# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLen = 0
        for i in range(len(s)):
            # odd length palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            # even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return res
        
if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))