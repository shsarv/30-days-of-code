class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        head = self.through_list(head, data)
        return(head)

    def through_list(self, current, data):
        if current is None: #True when head is None on the beggining
            nodo = Node(data)
            return(nodo)
        elif current.next is None: #True when is the last node on the list
            nodo = Node(data)
            current.next = nodo
            return(current)
        else: #True when is not the last node and you must advance
            current.next = self.through_list(current.next, data)
            return(current)
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
