# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


'''
    链表相关
'''


class SimpleChain(object):

    def __init__(self, value):
        self.value = value
        self.child = None

    def link(self, chain):
        """
            add chain
        :param chain:
        :return:
        """
        self.child = chain
        return chain

    # def __str__(self):
    #     s_chain = self.value
    #     chain = self.child
    #     while chain:
    #         s_chain = s_chain + '-->' + chain.value
    #         chain = chain.child
    #     return s_chain


def reverse(node):
    """

    :return:
    """
    while node:
        l


sc = SimpleChain('10')
sc.link(SimpleChain('127')).link(SimpleChain('0')).link(SimpleChain('11'))
print sc
print sc.reverse()
