#encoding:utf-8

# 问题描述：
# 给一个列表，给定一个数（target），找出这个列表中两个数相加等于target
# 返回两个数的下标，假定一定存在这样的两个数


def twosum(nums, target):
	dic = {}
	i = 0
	for a in nums:
		i += 1
		if dic.get(target-a, -1) > 0:
			return dic[target-a], i 
		dic[a] = i

num = [3, 2, 4]
print twosum(num, 6)
