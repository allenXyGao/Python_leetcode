# Leetcode 50. Pow(x, n)
'''
Example 1:

Input: 2.00000, 10
Output: 1024.00000
'''

class Solution(object):
    '''
    # method 1: brute force:TLE
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 3 cases:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = - n
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans
    '''
    
    '''
    # dfs TLE
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.helper(x, - n)
        return self.helper(x, n)
    
    def helper(self, x, n):
        if n == 1:
            return x
        left_pow = n // 2
        right_pow = n - left_pow
        ans = self.helper(x, left_pow) * self.helper(x, right_pow)
        return ans
    '''
    
    # improved: add a memory dict that store the value of x^n, if n has appeared in the
    # previous calculation so that we can avoid much repeated calculation.
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.helper(x, -n, {})
        return self.helper(x, n, {})
    
    def helper(self, x, n, memo):
        if n == 1:
            return x
        if n in memo:
            return memo[n]
        left_pow = n // 2
        right_pow = n - left_pow
        ans = self.helper(x, left_pow, memo) * self.helper(x, right_pow, memo)
        # store the value of x^n given n
        memo[n] = ans
        return ans