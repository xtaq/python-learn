#encoding:utf-8

# 问题描述
#Given a string, find the length of the longest substring without repeating characters.
#For example, the longest substring without repeating letters for "abcabcbb" is "abc",
#which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i = end = 0
        count = maxx = 0
        if len(s) == 0:
            return 0
        for c in s:
            if dic.get(c, -1) == -1:
                dic[c] = i
                count += 1
                if maxx < count:
                    maxx = count
            else:
                count = 0
                if end < dic[c]:
                    count += i - dic[c]
                else:
                    count += i - end
                if maxx < count:
                    maxx = count
                if end < dic[c]:
                    end = dic[c]
                dic[c] = i
            i += 1
        return maxx

