# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:23:47 2019

@author: LiuZiping
"""
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
def swapNodesInPairRecursion(head):
    """
    利用递归的思想，第一个节点的next是第三个和第四个节点交换的结果。第二个节点的next是第一个节点
    同理，第三个节点的next是第五个和第六个节点交换的结果，第四个节点的next是第三个节点。依次递归下去
    """
    if not head or not head.next:
        return head
    _next = head.next
    head.next = swapNodesInPairRecursion(_next.next)
    _next.next = head
    return _next

def swapNodesInpair(head):
    """
    遍历链表，以每两个节点为一组调换节点的顺序；
    注意虚拟节点的设置以及两个节点为一组时前一节点的next所指
    """
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    resultNode = dummy
    while dummy.next and dummy.next.next:
        first, second = dummy.next, dummy.next.next
        first.next = second.next
        dummy.next = second
        second.next = first
        dummy = dummy.next.next
    return resultNode.next

#if __name__ == "__main__":
#    first = ListNode(1)
#    second = ListNode(2)
#    third = ListNode(3)
#    fourth = ListNode(4)
#    first.next = second
#    second.next = third
#    third.next = fourth
#    result = swapNodesInpair(first)
        