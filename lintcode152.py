# lintcode 152 combinations
# Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n.
'''
Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 4, k = 1
Output: [[1],[2],[3],[4]]

'''

class Solution():
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def __init__(self):
        self.ans = []
    
    def combine(self, n, k):
        # corner case
        if n < k or n <= 0:
            return
        start_index = 0 
        combination = []
        nums = list(range(1, n+1))
        self.helper(n, k, nums, start_index, combination)
        return self.ans
    
    def helper(self, n, k, nums, start_index, combination):
        if len(combination) == k:
            self.ans.append(combination[:])
            return
        for i in range(start_index, n):
            combination.append(nums[i])
            self.helper(n, k, nums, i+1, combination)
            combination.pop()


# test case
S = Solution()
n = 4
k = 2
print(S.combine(n, k))

