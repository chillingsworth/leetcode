class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums, start=i):
                #Need to use permuation and not combination
                #Since each input has exactly one solution per the instructions
                ##can just check to see if the two indices are already in list before
                ##doing the check
                if (i not in indices and not j in indices) and \
                    n1 + n2 == target:
                    indices.append(i)
                    indices.append(j)
        return indices
