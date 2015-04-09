#coding:utf-8

#二分查找

l =[0, 3, 6, 12, 20, 28]  

def search(L, e):
    def bsearch(L, e, low, high):
        if low == high :
	    return L[low] == e
	mid = int((low + high)/2)
	if L[mid] == e :
	    return True
	if L[mid] > e :
	    return bsearch(L, e, low, mid-1) 
	else :
	    return bsearch(L, e, mid+1, high)
	
    if len(L) == 0 :
        return False
    else :
        return bsearch(L, e, 0, len(L)-1)

print search(l, 3)
print search(l, 28)
print search(l, 9)

