# Lintcode 135 Combination Sum I

'''
Description:
Given a set of candidtate numbers candidates and a target number target. 
Find all unique combinations in candidates where the numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Examples:
1.Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]

2.Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
'''


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # since we want find all unique cominations, we need to delete duplicates
        nums = list(set([2, 2, 3, 6, 7])) # remove duplicates
        nums.sort() # sort
        ans = []
        start_index = 0
        combination = []
        self.helper(nums, target, start_index, combination, ans)
        return ans
    
    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # （找到所有以 combination 开头的满足条件的组合，放到 results）
    def helper(self, nums, target, start_index, combination, ans):
        # the exit of recursive: target < 0
        if target < 0:
            return
        
        if target == 0:
            ans.append(combination[:])
            return
        
        # 递归的拆解
        for i in range(start_index, len(nums)):
            # [2] -> [2,2]
            combination.append(nums[i])
            self.helper(nums, target - nums[i], i, combination, ans)
            # [2,2] -> [2]
            combination.pop() # backtracking

# test case
S = Solution()
candidates = [2, 3, 6, 7]; target = 7  # [[7], [2, 2, 3]]
print(S.combinationSum(candidates, target))
