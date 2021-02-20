#duplet sum
def duplet2(l,k):
    l.sort()
    low=0
    high=len(l)-1
    while low<high:
        if l[low]+l[high] == k:
            print(l[low], l[high])
            break
        elif l[low]+l[high]<k:
            low+=1
        else:
            high-=1
    

def duplet(l,k):
    dict={}
    for i in range(len(l)):
        if (k-l[i]) in dict:
            print(l[i],k-l[i])
            break
        else:
            dict[l[i]] = i
#triplet sum
def triplet2(l,summ):
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                if l[i]+l[j]+l[k] == summ:
                    print(l[i],l[j],l[k])
                    break
                
    
def triplet(l,summ):
    l.sort()
    for i in range(len(l)-2):
        var = summ-l[i]
        low=0
        high=len(l)-1
        while low<high:
            if l[low]+l[high]==var:
                print(l[i],l[low],l[high])
                break
            elif l[low]<l[high]:
                low+=1
            else:
                high+=1
                
#sort012array
def sort_array(l):
    count=0
    low,high=0,len(l)-1
    mid = 0
    while mid<=high:
        if l[mid] == 0:
            l[mid],l[count]=l[count],l[mid]
            mid+=1
            count+=1
        elif l[mid]==2:
            l[mid],l[high] = l[high],l[mid]
            high-=1
        else:
            mid+=1
    print(l)
'''
def transpos():
    matrix=[]
    B=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    l=[]
    for i in range(4):
        l=list(map(int,input().split(' ')))
        matrix.append(l)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            B[i][j] = matrix[j][i]
    print(B)
transpos()
'''
            
#snakepattern
def snake_pattern(matrix):
    for i in range(len(matrix)):
        if i%2 !=0:
            for j in range(len(matrix)):
                print(str(matrix[i][j]))
        else:
            for j in range(len(matrix)-1,-1,-1):
                print(str(matrix[i][j]))

#MinPlatforms

#leadersinarray
def leaders(l):
    val=l[-1]
    d=[]
    d.append(val)
   
    for i in range(len(l)-1,-1,-1):
        if l[i]>val:
            d.append(l[i])
            val=l[i]
        else:
            pass
    print(*d)


def lastindexOfOne(l):
    var=0
    for i in range(len(l)):
        if l[i] == '1':
            var=i
            
    print(var)

def lastindexOfOne2(l):
    for i in range(len(l)-1,-1,-1):
        if l[i] == '1':
            print(i)
            break


def largestNumebrFormed(l):
    strr=""
    for i in range(len(l)):
        strr+=str(l[i])
    print(l)
    print(strr)
    print(''.join(sorted(strr)))

def kthsmallelement(l,k):
    l.sort(reverse=True)
    print(l[k])



def zigzag(l):
    flag=True
    for i in range(len(l)-1):
        if flag is True:
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
        else:
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
        flag= False
    print(l)



def spiralTraverse(l):
    left=0
    right=len(l)-1
    for i in range(left,right+1):
        print(l[0][i])
    for i in range(1,len(l)):
        print(l[i][3])
    for i in range(len(l)-2,-1,-1):
        print(l[3][i])
    for i in range(len(l)-2,0,-1):
        print(l[i][0])
    for i in range(1,len(l)-1):
        print(l[1][i])
    for i in range(len(l)-2,0,-1):
        print(l[2][i])
        


def printMaxOne(l):
    maxx=0
    largest=0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j]==1:
                count+=1
        if count>maxx:
            largest
    print(count)
            

#topologysort

from collections import defaultdict
class Graph:
    def __init__ (self,vertices):
        self.graph = defaultdict(list)
        self.V=vertices
    def addedge(self,u,v):
        self.graph[u]=v
    def topologyUtil(self,v,visited,stack):
        visited[v] == True:
        for i in graph[v]:
            if visited[i] == False:
                self.topologyUtil(i,visited,stack)
        stack.insert(0,v)

    def topologysort(self):
        visited=[]
        stack=[]
        for i in range(self.v):
            if visited[v]== False:
                topologyUtil(v,visited,stack)
        print(stack)
            
            
            


'''
    
l=list(map(int,input().split()))
zigzag(l)
#largestNumebrFormed(l)
l=list(map(int,input().split()))
k=int(input())
kthsmallelement(l,k)'''

    
#l=list(map(int,input().split()))
#leaders(l)
#l=input()
#lastindexOfOne(l)
#lastindexOfOne2(l)
    
'''
#l = list(map(int,input().split(' ')))
#k = int(input())
#triplet(l,k)
#sort_array(l)
'''
l=[]
matrix=[]
for i in range(4):
    l=list(map(int,input().split(' ')))
    matrix.append(l)
spiralTraverse(matrix)

#snake_pattern(matrix)
















    
