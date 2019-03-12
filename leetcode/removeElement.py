# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    算法描述:
   
'''



class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def str(self):
        v = self
        vs = []
        while v:
            vs.append(v.val)
            v = v.next
        return vs


def removeLinked(head, val):
    prev, cur = None, head
    while cur:
        if cur.val == val:
            if prev is None:
                head = cur.next
            else:
                prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    if head:
        return head.str()
    else:
        return []


def removeArray(array, value):
    p = i = 0
    length = len(array)
    for i in xrange(length):
	if array[i] == value:
           array[i], array[p] = array[p], array[i]
	   p += 1
    return array[:p+1]

h = ListNode(1)
h2 = ListNode(1)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)
h.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
print removeLinked(h, 1)
