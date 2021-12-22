class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def swap(c, i, j):
            c = list(c)
            c[i], c[j] = c[j], c[i]
            return ''.join(c)
        
        valid_strings = []

        seed = ''.join(['(' for i in range(n)]) + \
        ''.join([')' for i in range(n)])
        
        valid_strings.append(seed)
        
        right_ptr = n
        left_ptr = n-1
        
        left = True
        
        while left_ptr > 0 and right_ptr < len(seed) - 1:
            seed = swap(seed, left_ptr, right_ptr)
            if seed not in valid_strings:
                valid_strings.append(seed)
            if left == True:
                left_ptr -= 1
                right_ptr -= 1
            else:
                left_ptr += 1
                right_ptr += 1
            if left_ptr == 0:
                left = False
                right_ptr = n
                left_ptr = n-1

        return valid_strings
        