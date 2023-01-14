#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self,key = None, next = None):
        self.key = key
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
class BinaryNode:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
class ADL_tree:
    def __init__(self,data = None):
        self.root = None
        self.head = None
        self.size = 0
    def add(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1
        
    def ADL_1(self):
        a = []
        if self.head == None:
            self.root == None
            raise valueerror('NoElement')
        self.root = BinaryNode(self.head.key)
        a.append(self.root)
        while self.head.next != None:
            parent = a.pop(0)
            self.head = self.head.next
            leftChild = BinaryNode(self.head.key)
            a.append(leftChild)
            if self.head.next != None:
                    self.head = self.head.next
                    rightChild = BinaryNode(self.head.key)
            a.append(rightChild)
            parent.left = leftChild
            parent.right = rightChild
      
        
    def inorderTraversal(self, root):
        if root != None:
            self.inorderTraversal(root.left)
            print (root.data,end=" ")
            self.inorderTraversal(root.right)
            
    def get_node(self,i):
        if i<0 or i>self.size:
            raise IndexError("Error")
        if self.size == 0:
            raise IndexError("Error")
        idx = 0
        walk = self.head
        while idx < i:
            walk = walk.next
            idx += 1
        return walk
    def getParent(self,i):
        assert i >= 1
        parent = self.get_node((i-1)//2) 
        return parent
    def getLeftChild(self,i):
        assert i >= 0
        leftChild = self.get_node(2*i+1)
        return leftChild
        
    def getRightChild(self,i):
        assert i >= 0
        rightChild = self.get_node(2*i+2)
        return rightChild
       
        
        
        
b = ADL_tree()
b.add(15)
b.add(30)
b.add(2)
b.add(34)
b.add(56)
b.add(13)
b.add(14)
print(b.getRightChild(0))
b.ADL_1()

print ("Inorder Traversal of the constructed Binary Tree is:")
b.inorderTraversal(b.root)

                
                
        
        
            
        
        
        


# In[15]:


#design minimum priority queue
''' design minority priority queue:
   find leaf nodes and compare leaf nodes with their parent node, 
   smaller than parent node, then swap position till it is bigger than its parent node'''     
class Min_Queue:
    def __init__(self):
        # get a complete binary tree
        self.head = None
        self.root = None
        self.size = 0
    def get_node(self,i):
        if i<0 or i>self.size:
            raise IndexError("Error")
        if self.size == 0:
            raise IndexError("Error")
        idx = 0
        walk = self.head
        while idx < i:
            walk = walk.next
            idx += 1
    def heapify(self):
        #heapify into min heap
        if self.size == 0 or self.size == 1:
            return
        assert self.head != None
        for i in range(1,self.size):
            par = int((i-1)/2)
            if par == 0:
                if self.get_node(par).key > self.get_node(i).key:
                    self.get_node(i).next = self.get_node(par)
                    self.get_node(par).next = self.get_node(i+1)    
            else:
                while (int(par) - 1) >= 0 and (int(par) + 1) <= self.size and i + 1 <= self.size:
                    if self.get_node(par).key > self.get_node(i).key:
                        self.get_node(i).next = self.get_node(int(par) + 1)
                        self.get_node(par-1).next = self.get_node(i)
                        self.get_node(par).next = self.get_node(i + 1)
                        self.get_node(i-1).next = self.get_node(par)
        
                
    def findMindx(self):
             # find smallest node's index in LinkedList
        if self.head == None:
            raise IndexError('NoElement')
        a = [self.head]
        idx = 0
        walk = self.head
        while walk.next != None and len(a)!= 0:
            walk = walk.next
            idx += 1
            if a.pop(0).key > walk.key:
                a.append(walk)
                return 0
        return idx 
    def insert(self,data):
        new_node = Node(data)
        # put new_node in the LinkedList's tail , so new_node is a leave node
        if self.head == None :
            self.head = new_node
            self.size += 1
        else:   
            walk = self.head
            while walk.next != None:
                walk = walk.next
            walk.next = new_node
            self.size += 1
        self.heapify()
    def delMin(self): # find last node and then put it at self.head, then heapify
        if self.head == None:
            raise ValueError('error')
        if self.size == 1 :
            self.head = None
        walk = self.head
        while walk.next != None:
            walk = walk.next
        walk = self.head
        walk = None
        self.heapify()
       
    

        
        
        
''' time complexity of insert() and delMin() both are O(log(n))
                     '''
           
                    
            
            
            
# visualize heap based on LinkedList
a = Min_Queue()
a.insert(3)
a.insert(2)
a.insert(5)
a.insert(11)
a.insert(23)
a.insert(8)
a.insert(9)
a.insert(15)
a.ADL_1()
print ("Inorder Traversal of the constructed Binary Tree is:")
a.inorderTraversal(a.root)

                
                                
                                
                        
                        
                    
            
        
    
    


# In[ ]:


def heapify(self,n,i): # n is the size of LinkedList
        sml = i # Initialize samllest as root
        l = 2*i + 1
        r = 2*i + 2
        if l < n and get_node(self,l).key < get_node(self,i): #left child smaller than sml
            sml = l
        elif r < n and get_node(self,r).key < get_node(self,i): # right child smaller than sml
            sml = r
        elif sml != i: 
            n1 = get_node(self,i-1)
            n2 = get_node(self,sml-1)
            get_node(self,sml).next = get_node(self,i+1)
            n1.next = get_node(self,sml)
            get_node(self,i).next = get_node(self,sml+1)
            n2.next = get_node(self,i)
        return heapify(self,n,sml)

