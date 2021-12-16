class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        buffer = ''        
        longest_palindrome = s[0]
        
        for i, c in enumerate(s):
            buffer+=c
            if len(s) - i < len(longest_palindrome):
                break
            for j, d in enumerate(s, i+1):
                if j <= len(s) - 1:
                    buffer+=s[j]
                    if buffer == buffer[::-1] and \
                    len(buffer) > len(longest_palindrome):
                        longest_palindrome = buffer
            buffer=''
        
        return longest_palindrome
