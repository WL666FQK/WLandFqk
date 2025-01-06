# Author: 王璐
# Date: 2024/12/25

# 完成二叉树的层次建树，并实现前序遍历，中序遍历，后序遍历
import random


class Node:
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild

class Tree:
    def __init__(self):
        self.root=None
        self.queue=[]

    def insert_node(self,elem):
        new_node=Node(elem)  # 对新结点初始化
        self.queue.append(new_node)  # 把新结点插入队列
        if self.root is None:
            self.root=new_node
        else:
            # 若左孩子为空，新结点是左孩子；若左孩子不为空，右孩子为空，新结点是右孩子。插入完右孩子，该队列第一个结点的左右孩子都不为空，弹出第一个结点
            if self.queue[0].lchild is None:
                self.queue[0].lchild=new_node
            else:
                self.queue[0].rchild=new_node
                self.queue.pop(0)

    # 先序遍历
    def preorder(self,current_node:Node):
        if current_node is not None:
            print(current_node.elem,end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    # 中序遍历
    def inorder(self, current_node: Node):
        if current_node is not None:
            self.inorder(current_node.lchild)
            print(current_node.elem, end=' ')
            self.inorder(current_node.rchild)

    # 后序遍历
    def lastorder(self, current_node: Node):
        if current_node is not None:
            self.lastorder(current_node.lchild)
            self.lastorder(current_node.rchild)
            print(current_node.elem, end=' ')

if __name__ == '__main__':
    tree=Tree()
    for i in range(1,7):
        tree.insert_node(i)
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.lastorder(tree.root)

