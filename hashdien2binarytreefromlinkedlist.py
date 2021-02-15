class linkedlist:
    def __init__ (self,data):
        self.data=data
        self.next = None
class binary:
    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None

class conversion:
    def __init__ (self):
        self.head = None
        self.root = None

    def push(self,data):
        if self.head ==None:
            newnode = linkedlist(data)
            newnode.next = self.head
            self.head = newnode
            self.head.next = None
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            newnode = linkedlist(data)
            temp.next = newnode
            newnode.next = None

    def convert(self):
        q=[]
        if self.head == None:
            self.root= None
            return
        self.root=binary(self.head.data)
        q.append(self.root)
        temp = self.head.next
        while temp:


            parent = q.pop()
            left = None
            right = None

            left= binary(temp.data)
            q.append(left)
            temp = temp.next
            if temp:
                right = binary(temp.data)
                q.append(right)
                temp=temp.next

            parent.left = left
            parent.right=right
            
            

    def inorder(self,root):
        if root is None:
            return -1
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            

conv = conversion() 
conv.push(36) 
conv.push(30) 
conv.push(25) 
conv.push(15) 
conv.push(12) 
conv.push(10) 
  
conv.convert() 
  
print ("Inorder Traversal of the contructed Binary Tree is:")
conv.inorder(conv.root) 
                























        
