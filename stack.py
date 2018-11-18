# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    链表相关面试:
    1 链表构建
    2 链表反转
'''


class Chain(object):
    def __init__(self, value):
        self.value = value
        self.child = None

    def link(self, child):
        self.child = child
        return child

    def reverse(self):
        next_node = None
        node = self
        while node:
            child = node.child
            node.link(next_node)
            next_node = node
            node = child
        return next_node

    def __str__(self):
        node_list = []
        node = self
        while node:
            node_list.append(node.value)
            node = node.child
        return '.'.join(node_list)


h = Chain('10')
h.link(Chain('127')).link(Chain('0')).link(Chain('11'))
print h
print h.reverse()

