# Leetcode 301. Remove Invalid Parentheses
'''
Remove the minimum number of invalid parentheses in order to make the input string valid. 
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
'''


class Solution(object):
    
    def __init__(self):
        self.output = []
        self.patterns = [['(', ')'], [')', '(']]
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        #start, lastRemove = 0, 0
        self.dfs(s, 0, 0, self.patterns[0])
        return self.output
    
    def dfs(self, s, start, lastRemove, pattern):
        
        cnt = 0
        n = len(s)
        # search from start
        for i in range(start, n):
            if s[i] == pattern[0]:  # '('
                cnt += 1
            if s[i] == pattern[1]:  # ')'
                cnt -= 1
            if cnt < 0:
                # 右括号多了，此时要开始搜索了。 从lastRemove开始删一个右括号直到i为止
                # i 不合法噢
                for j in range(lastRemove, i+1):
                    if s[j] == pattern[1] and (j == lastRemove or s[j] != s[j-1]):
                        # 删除j处的字符并带入dfs
                        
                        self.dfs(s[0:j] + s[j+1:], i, j, pattern)
                return
            
            
        # 正向扫描合法，但反向不合法，即左括号》右括号
        s = ''.join(list(reversed(s)))
        if pattern[0] == self.patterns[0][0]:
            self.dfs(s, 0, 0, self.patterns[1])
        else:
            self.output.append(s)