#encoding:utf-8

# 问题描述
# 把字符串转换为整数，从是数字的开头到不是数字结尾，考虑正负号，空串

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if len(str)==0:
            return 0
        str = str.strip()
        request = 0
        first = 0
        sign = 1
        if str[0] != '-' and str[0] != '+':
            if str[0] < '0' or str[0] > '9':
                return 0
            else:
                first = int(str[0])
        elif str[0] == '-':
            sign = -1
        request = request + first
        for i in range(1, len(str), 1):
            if str[i] >= '0' and str[i] <= '9':
                request = request * 10 + int(str[i])
            else:
                break
        if request*sign > 2147483647:
            return 2147483647
        if request*sign < -2147483648:
            return -2147483648
        return request*sign
