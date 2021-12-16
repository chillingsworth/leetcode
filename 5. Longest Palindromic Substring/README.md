# 5. Longest Palindromic Substring

## Successful Attempts: 0

## Failed Attempts: 1

## Notes
Following is solution used from leetcode:

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
```

I'm also updating the my_solution.py file to include my original solution to this problem as per my new 'how to read' guidelines in the main repo README.md.

See github commit from the original submission for original notes.
