#coding:utf-8

#选择排序

l = [10, 23, 8, 4, 91, 44, 81]

def selsort(L):
    for i in range(len(L)) :
        mini = i
	minval = L[i]
	j = i + 1
	
	while j < len(L) :
	    if minval > L[j] :
	        mini = j
		minval = L[j]
	    j += 1
	
	temp = L[i]
	L[i] = minval
	L[mini] = temp

selsort(l)
for i in l : 
    print i

