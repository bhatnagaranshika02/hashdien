class tree:
    def __init__ (self,data):
        self.data = data
        self.left = left
        self.right = right

class solution:
    def __init__(self):
        self.root = None
        self.root2 = None
        self.parent=None
    def identical(self,n1,n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        if n1.data != n2.data:
            return False
        else:
            return (identical(n1.right,n2.right) and identical(n1.left,n2.left))

    def height(self,n1):
        if n1 is None:
            return 0
        else:
            return 1+ max(height(self.left),height(self.right))

    def heightIterative(self,n1):
        q=[]
        q.append(n1)
        count=0
        while q is not None:
            size=len(q)
            while size>0:
                var = q.pop()
                if var.left:
                    q.append(var.left)
                if var.right:
                    q.append(var.right)
                size-=1
            count+=1
        return count

    def cousins(self,a,b):
        if self.root is None:
            return 0
        return ((root.left==a and root.right==b) or root.left == b and root.right==a)
                or cousins(root.left,a,b)or cousins(root.right,a,b)

    def level(sef,ptr,lev):
        if self.root is None:
            return 0
        if root == ptr:
            return lev
        l=level(root.left,ptr,lev+1)
        if l!=0:
            return l
        return level(root.right,ptr,lev+1)

    def issiblings(self,a,b):
        if (level(a,1) == level(b,1)) and not(cousins(a,b)):
            return 1
        else:
            return 0

    def lowest_common_anscestor(self,n1,n2):
        ans=[]
        temp=n1
        while temp!=None:
            temp=temp.parent
            if temp!=None:
                ans.append(temp)
        temp=n2
        while temp!=None:
            temp=temp.parent
            for i in range(0,len(ans)):
                if ans[i] ==temp:
                    print(temp)
                    return temp
        return None
    def lowestCA(self,n1,n2):
        if root is None:
            return None
        elif root==n1 or root==n2:
            return root
        left = lowestCA(temp.left,n1,n2)
        right=lowestCA(temp.right,n1,n2)
        if left!=None and right!=None:
            return temp
        elif(left_subtree!=None):
            return left_subtree
        else:
            return right_subtree






        











        
        
        
        












    
