'''
单链表练习
'''
class Node(object):
    """单链表的结点"""

    def __init__(self, item=0, next=None):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = next


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        # 头节点不保存具体数值
        self._head = Node()

    def append(self, node: Node):
        # 尾插入
        cur = self._head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def items(self):
        # 循环遍历
        cur = self._head.next
        while cur is not None:
            # 返回生成器
            yield cur.item
            cur = cur.next

    def insert(self, index, node: Node):
        # index为索引，从0开始
        count = 0
        cur = self._head
        while cur is not None:
            if count == index:
                node.next = cur.next
                cur.next = node
                return True
            count += 1
            cur = cur.next
        return False

    def add(self, node: Node):
        cur = self._head.next
        node.next = cur
        self._head.next = node


if __name__ == '__main__':
    link_list = SingleLinkList()
    node_1 = Node(1)
    node_2 = Node(2)
    link_list.append(node_1)
    link_list.append(node_2)
    for i in link_list.items():
        print(i) # 输出1 2

    node_3 = Node(3)
    link_list.insert(0, node_3)  # 输出3 1 2
    for i in link_list.items():
        print(i)

    node_4 = Node(4)
    link_list.add(node_4) #输出4 3 1 2
    for i in link_list.items():
        print(i)
