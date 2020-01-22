# Lintcode 153 Combination Sum II
'''
Description:
Given an array num and a number target. 
Find all unique combinations in num where the numbers sum to target.

Examples:
1. Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

2. Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.

Note:
Each number in num can only be used once in one combination.
All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.

'''

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, nums, target):
        if not nums:
            return
        nums.sort()
        ans = []
        start_index = 0
        combination = []
        self.dfs(nums, target, start_index, combination, ans)
        return ans
    
    def dfs(self, nums, target, start_index, combination, ans):
        if target < 0:
                return
        if target == 0 and combination not in ans:
            ans.append(combination[:])
            return
        
        for i in range(start_index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, target - nums[i], i+1, combination, ans)
            combination.pop()

