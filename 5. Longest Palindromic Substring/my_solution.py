class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        buffer = ''
        palindromes = []
        
        palindromes.append(s[0])
        
        for i, c in enumerate(s):
            buffer+=c
            for j, d in enumerate(s, i+1):
                if j <= len(s) - 1:
                    buffer+=s[j]
                    if buffer == buffer[::-1]:
                        palindromes.append(buffer)
            buffer=''
        
        return max(palindromes, key=len)