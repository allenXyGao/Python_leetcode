# Lintcode 17 Subset
# Given a set of distinct integers, return all possible subsets.


'''
Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # 想要所有的子集，也就是搜索所有的长度从1到length(nums)的组合，即combination
        ans = []
        if not nums:
            return [ans]
        for l in range(len(nums)+1):
            combination = []
            start_index = 0
            self.dfs(nums, l, start_index, combination ,ans)
        return ans
    
    def dfs(self, nums, length, start_index, combination, ans):
        if len(combination) == length:
            ans.append(combination[:])
            return
        
        for i in range(start_index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, length, i+1, combination, ans)
            combination.pop()

S = Solution()
nums = [1,3,9]  
'''
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
S.subsets( nums)