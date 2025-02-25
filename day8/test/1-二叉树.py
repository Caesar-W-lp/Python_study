# 作者:李一安
# 2025年02月23日13时23分01秒


class Node:
    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        # 辅助队列用于记录待分配子节点的父节点
        self.parent_queue = []

    def level_build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.parent_queue.append(node)

        else:
            # 将这一代的非父节点存入队列作为下一代的父节点
            self.parent_queue.append(node)

            # 查看父节点下辖的左右子节点哪个空闲，插入新节点
            if self.parent_queue[0].lchild is None:
                self.parent_queue[0].lchild = node

            else:
                # 左子树已满，则插入右子树
                self.parent_queue[0].rchild = node
                self.parent_queue.pop(0) # 当前父亲满了，弹出父亲，准备插入下一层节点

    # 深度优先遍历：先序遍历、中序遍历、后序遍历
    # 前序遍历
    def pre_order(self, current_node: Node):
        if current_node:
            print(current_node.elem, end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    # 中序遍历
    def mid_order(self, current_node: Node):
        if current_node:
            self.mid_order(current_node.lchild)
            print(current_node.elem, end=' ')
            self.mid_order(current_node.rchild)

    # 后序遍历
    def post_order(self, current_node: Node):
        if current_node:
            self.post_order(current_node.lchild)
            self.post_order(current_node.rchild)
            print(current_node.elem, end=' ')


    # 广度优先遍历：层次遍历
    def level_order(self):
        # 根节点入队
        help_queue = []
        help_queue.append(self.root)

        while help_queue:
            out_node : Node = help_queue.pop(0) # 出队
            print(out_node.elem, end=' ') # 打印出队元素
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)


if __name__ == '__main__':
    # 实例化树
    tree = BinaryTree()

    # 构造树
    for i in range(1, 11):
        # 实例化节点
        new_node = Node(i)

        # 把节点放入树中
        tree.level_build_tree(new_node)

    # 先序遍历
    print('先序遍历：')
    tree.pre_order(tree.root)

    # 中序遍历
    print('\n中序遍历：')
    tree.mid_order(tree.root)

    # 后序遍历
    print('\n后序遍历：')
    tree.post_order(tree.root)

    # 层次遍历
    print('\n层次遍历：')
    tree.level_order()






# 总结：
# 由于python中一切皆对象，所以所有的函数传参都是传递对象的引用，而非整个对象
# 实参记录的是原本对象的引用，形参记录的是实参的副本，即这个对象引用的副本
# 再进一步就要考虑可变数据类型和不可变数据类型对于形参改变的影响
# 当实参为可变数据类型引用，则形参也为可变数据类型引用，在函数内部对形参进行修改时，是对其指向的对象进行修改，则实参指向的对象也会发生改变
# 当实参为不可变数据类型引用，则形参也为不可变数据类型引用，在函数内部对形参进行修改时，会修改形参指向的对象为修改后的对象，但实参仍然指向原来的对象，不会发生改变
# 实例对象是可变数据类型
# 递归循环是while循环的一个+变种