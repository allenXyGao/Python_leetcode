# Leetocde 1239. Maximum Length of a Concatenated String with Unique Characters
'''
Description:
Given an array of strings arr. 
String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.

test case:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

'''

class Solution:
    # dfs: 思路是暴力搜索所有的字母组合, 相当于是subset
    # result: very slow
    
    def maxLength(self, arr):
        if not arr or len(arr) == 0:
            return 
        self.max_length = 0
        for l in range(1, len(arr)+1):
            start_index = 0
            path = []
            self.dfs(arr, l, start_index, path)
        return self.max_length

    
    def dfs(self,  arr, length, start_index, path):
        if not self.validate(''.join(path)):
            return
    
        if len(path) == length:
            self.max_length = max(self.max_length, len(''.join(path)))
            return
        
        for i in range(start_index, len(arr)):
            path.append(arr[i])
            self.dfs(arr, length, i+1, path)
            path.pop()
        
 
    def validate(self, string):
        hash = {}
        for s in string:
            hash[s] = hash.get(s, 0) + 1
            if hash[s] >= 2:
                return False
        return True


# Method 2:

class Solution:
    # set
    def maxLength(self, arr):
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a):  # if there are duplicate char, pass!
                continue
            currUsed = set(a)
            for used in dp[:]:
                if len(used & currUsed) == 0:  
                    dp.append(used | currUsed)
        return len(max(dp, key=len))