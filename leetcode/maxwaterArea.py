#encoding:utf-8

# 问题描述
# 给一个整数数组，代表高度，求两个高度最小的那个和下标差的乘积的最大值
# 头尾两个指针，最大长度，当高度大于头尾时，面积才有可能更新
# 所以线性扫描一遍，即可更新状态，求出最大值

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maxx = 0
        l = 0
        r = len(height) - 1
        while l < r:
            maxx = max(maxx, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                k = l
                while k < r and height[k] <= height[l]:
                    k += 1
                l = k
            else:
                k = r
                while k > l and height[k] <= height[r]:
                    k -= 1
                r = k

    return maxx