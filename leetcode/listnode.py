#encoding:utf-8

# 问题描述
# 两个链表，按位相加，返回相加后的链表，有进位

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        a = ListNode((l1.val + l2.val) % 10)
        l = a
        p = l1.next
        q = l2.next
        f = (l1.val + l2.val)/10
        while p and q:
            l.next = ListNode((p.val + q.val + f) % 10)
            f = (p.val + q.val + f)/10
            p = p.next
            q = q.next
            l = l.next
        while p:
            l.next = ListNode((p.val + f) % 10)
            f = (p.val + f)/10
            p = p.next
            l = l.next
        while q:
            l.next = ListNode((q.val + f) % 10)
            f = (q.val + f)/10
            q = q.next
            l = l.next
        if f:
            l.next = ListNode(f)
        return a
