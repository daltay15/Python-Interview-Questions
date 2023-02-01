# Description: Given two strings s and t , write a function to determine if t is an anagram of s.



class Solution:
    
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):    # If the lengths are not equal
            return False    # Return false

        
        countS, countT = {}, {} # Create two hashmaps

        for i in range(len(s)): # Iterate through the strings
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Add the character to the hashmap
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Add the character to the hashmap
        for c in countS:    # Iterate through the hashmap
            if countS[c] != countT.get(c,0):    # If the character is not in the other hashmap
                return False    # Return false
        
        return True # If the character is in the other hashmap,

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution.isAnagram(s,t))