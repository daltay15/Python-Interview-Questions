# 125. Valid Palindrome
# Difficulty: Easy
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



class Solution:
    
    # less memory efficient
    def isPalindromeEasy(s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1] # reverse string


    # more memory efficient using two pointers
    def isPalindromeHarder(s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True




if __name__ == "__main__":
    s: str = "A man, a plan, a canal: Panama"
    print("Easy: ", Solution.isPalindromeEasy(s))
    print("Harder: ", Solution.isPalindromeHarder(s))