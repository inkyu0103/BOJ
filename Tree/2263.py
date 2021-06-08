# 2263
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def preorder(root):
    print(root, end=' ')
    if not root.left == None : preorder(root.left)
    if not root.right == None : preorder(root.right)


# inorder(start,end) , postorder(start,end)
def sol(inorder_idx,postorder_idx):
    if inorder_idx[0] == inorder_idx[1]:
        return Node(Inorder[inorder_idx[0]])

    criteria_idx = Inorder.index(Postorder[postorder_idx[1]])
    root = Node(Postorder[postorder_idx[1]])
    right = None
    left = None


    # exist left and right subtree
    if inorder_idx[0] < criteria_idx < inorder_idx[1]:
        left = sol((inorder_idx[0],criteria_idx-1),(postorder_idx[0],postorder_idx[0]+criteria_idx-inorder_idx[0] -1))
        right = sol((criteria_idx + 1, inorder_idx[1]), (postorder_idx[1] - 1 - (inorder_idx[1] - (criteria_idx+1)), postorder_idx[1] - 1))

    # only exist right subtree
    elif inorder_idx[0] == criteria_idx :
        left = None
        right = sol((criteria_idx+1,inorder_idx[1]),(criteria_idx,postorder_idx[1]-1))

    # only exist left subtree
    elif inorder_idx[1] == criteria_idx:
        left = sol((inorder_idx[0],criteria_idx-1),(postorder_idx[0],postorder_idx[0]+criteria_idx-inorder_idx[0] -1))
        right = None

    root.right = right
    root.left = left

    return root

if __name__ == "__main__" :
    V = int(input())
    Inorder = list(map(int,input().split()))
    Postorder = list(map(int,input().split()))

    root = sol((0,len(Inorder)-1),(0,len(Inorder)-1))
    preorder(root)

