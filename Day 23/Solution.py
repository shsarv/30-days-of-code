import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    from collections import deque    
    def levelOrder(self,root):
        queue = self.deque([root])                     
  
        while queue :                              
            front = queue.popleft()                  
            print(front.data , end=" ")
            if front.left :queue.append(front.left)          
            if front.right : queue.append(front.right)

T=int(input())
