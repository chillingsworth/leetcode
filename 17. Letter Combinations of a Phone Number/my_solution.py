class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        digit_list = [d for d in digits]
        
        def unpack(digit_list):
            try:
                print(digit_list)
                msd = digit_list.pop(0)
                unpacked = unpack(digit_list)
                key_letters = [l for l in numbers[msd]]
                
                if unpacked != None:
                    combined = []
                    for key_letter in key_letters:
                        for unpacked_string in unpacked:
                            combined.append(key_letter + unpacked_string)
                    return combined
                else:
                    return key_letters

            except Exception as e:
                print('Empty list: ', e)
                return None
            
        combinations = unpack(digit_list)
        
        return combinations