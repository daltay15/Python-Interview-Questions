# 125. Valid Palindrome
# Difficulty: Easy
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



class Solution:
    
    # less memory efficient
    def isPalindromeEasy(s: str) -> bool:   
        newStr = "" # create new string

        for c in s: # iterate through string
            if c.isalnum(): # if alphanumeric
                newStr += c.lower() # add to new string
        
        return newStr == newStr[::-1] # reverse string


    # more memory efficient using two pointers
    def isPalindromeHarder(s: str) -> bool:
        left = 0    # initialize left pointer
        right = len(s) - 1  # initialize right pointer

        while left < right: # while left pointer is less than right pointer
            if not s[left].isalnum():   # if not alphanumeric
                left += 1   # increment left pointer
            elif not s[right].isalnum():    # if not alphanumeric
                right -= 1  # decrement right pointer
            elif s[left].lower() != s[right].lower():   # if not equal
                return False    # return false
            else:   # if equal
                left += 1   # increment left pointer
                right -= 1  # decrement right pointer
        
        return True 




if __name__ == "__main__":
    s: str = "A man, a plan, a canal: Panama"
    print("Easy: ", Solution.isPalindromeEasy(s))
    print("Harder: ", Solution.isPalindromeHarder(s))