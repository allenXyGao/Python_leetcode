# Leetcode 22. Generate Parentheses
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    '''
    We can (1). start an opening bracket if we still have one (of n) left to place. 
    (2). And we can start a closing bracket if it would not exceed the number of opening brackets.
    '''
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return
      
        self.output = []
        cur_list = ""
        left_num, right_num = 0, 0
        self.dfs(n, cur_list, left_num, right_num)
        return self.output
    
    
    def dfs(self, n, path, left_num, right_num):
        # the exit of dfs:
        if left_num == n and right_num == n:
            self.output.append(''.join(path))
            return
        if left_num < n:
            self.dfs(n, path + "(", left_num + 1, right_num)
        if right_num < n and right_num < left_num:
            self.dfs(n, path + ")", left_num, right_num+1)
        