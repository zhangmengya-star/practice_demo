'''
合并两个有序的单链表
'''


class Node(object):
    """单链表的结点"""

    def __init__(self, item=0, next=None):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = next


class Solution:
    def merge(self, l1: Node, l2: Node) -> Node:

        p = l1
        q = l2
        head = Node()
        r = head

        while p is not None and q is not None:
            if p.item < q.item:
                r.next = p
                r = r.next
                p = p.next
            else:
                r.next = q
                r = r.next
                q = q.next
        if p is not None:
            r.next = p
        if q is not None:
            r.next = q
        return head.next


if __name__ == '__main__':
    list_1 = Node()
    p = list_1
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    p.next = node_1
    p = p.next
    p.next = node_2
    p = p.next
    p.next = node_3
    p = p.next

    list_2 = Node()
    p = list_2
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    p.next = node_1
    p = p.next
    p.next = node_2
    p = p.next
    p.next = node_3
    p = p.next

    solution = Solution()
    result = solution.merge(list_1.next, list_2.next)
    print(result.item)
    print(result.next.item)
    print(result.next.next.item)
    print(result.next.next.next.item)
    print(result.next.next.next.next.item)
    print(result.next.next.next.next.next.item)
