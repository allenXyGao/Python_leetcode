# Lintcode_10 string permutation II

'''
Given a string, find all permutations of it without duplicates. 
Examples:
1. Input: "abb"
Output:
["abb", "bab", "bba"]

2. Input: "aabb"
Output:
["aabb", "abab", "baba", "bbaa", "abba", "baab"]
'''

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # 这道题最难的地方在于如果string中出现duplicate字母，该选哪一个置换
        # 所以先排序，而'str' object has no attribute 'sort'
        # 所以应该先转为list, 并且在dfs中append result时用 ''.join() 连接
        ans = []
        string = list(str)
        string.sort()
        
        permutation = []
        visited = set([])
        self.dfs(string, permutation, visited, ans)
        
        return ans
    
    def dfs(self, string, permutation, visited, ans):
        
        if len(permutation) == len(string):
            ans.append(''.join(permutation))
            return
        
        for i in range(len(string)):
            if i in visited:
                continue
            
            if i > 0 and string[i] == string[i-1] and i-1 not in visited:
                continue
                
            visited.add(i)
            permutation.append(string[i])
            self.dfs(string, permutation, visited, ans)
            visited.remove(i)
            permutation.pop()
            
S = Solution()
str = "abc"  # ["abb", "bab", "bba"]
S.stringPermutation2(str)