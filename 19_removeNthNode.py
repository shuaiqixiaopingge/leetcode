# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:32:09 2019

@author: LiuZiping
"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
def deleteNthNode(head, n):
    p = ListNode(0)
    p.next = head
    dummy = p
    q = head
    for i in range(n):
        q = q.next
    while q != None:
        p = p.next
        q = q.next
    p.next = p.next.next
    return dummy.next