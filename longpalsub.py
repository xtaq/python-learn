#encoding:utf-8

# 问题描述
# 求最长回文字串
# 找出所有回文串的中心可能位置，一共有2*len(s)－1个位置，然后对每个位置
#向两个方向匹配。

def lenpal(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

    
def longestPalindrome(s):
    if len(s) == 0:
        return ''
    maxlen = 0
    res = ''
    for i in range(2*len(s)-1):
        left = i/2
        right = i/2
        if i%2 == 1:
            right += 1
        spal = lenpal(s, left, right)
        if maxlen < len(spal):
            maxlen = len(spal)
            res = spal
    return res

print longestPalindrome('abb')
