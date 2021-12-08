class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        buffer = []
        for i, c in enumerate(s):
            buffer.append(c)
            for j, d in enumerate(s, i+1):
                if j <= len(s)-1 and s[j] not in buffer:
                    buffer.append(s[j])
                else:
                    break
            if len(buffer) > longest:
                longest = len(buffer)
            buffer.clear()
        return longest