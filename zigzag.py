# encoding:utf-8

# 问题描述：
# 把一个字符串zig旋转，先向下，再对角线向上，再向下...按每一行从新排列字符串，给定行数和一个字符串。

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        res = []
        for a in range(numRows):
            res.append('')
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    res[j] += s[i]
                    i += 1
            for j in range(numRows-2, 0, -1):
                if i < len(s):
                    res[j] += s[i]
                    i += 1
        return ''.join(res)
