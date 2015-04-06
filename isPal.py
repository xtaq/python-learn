#coding:utf-8

#判断回文串程序

def isPal(s) :
	#把字符串s转换为只有小写字符的串	
	def toChar(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans += c
		return ans
	#递归判断是否回文	
	def isp(s):
		if len(s) <= 1:
			return True
		else:
			#－1代表字符串最后一个字符，s［1:－1］去除首尾	
			return s[0] == s[-1] and isp(s[1:-1])
	#返回判断	
	return isp(toChar(s))

print isPal('abccba')
print isPal('hekhfbvke')
print isPal('aacdfdcaa')

