def bubble(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print(l)


def optim_bubble(l):
    for i in range(len(l)):
        swap=False
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swap=True
        if swap == False:
            break
        else:
            continue
    print(l)

def selection(l): 
    for i in range(len(l)):
        minn = i
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                minn = j
        l[minn],l[i] = l[i],l[minn]
    print(l)

def insertion(l):
    for i in range(1,len(l)):
        j=i
        key=l[i]
        while j!=0 and l[i] > key:
            l[j+1] = l[j]
            j-=1
    print(*l)

def Partition(l,low,high):
    i = low-1
    pivot = high
    for j in range(low,high):
        if l[j]<l[pivot]:
            i+=1
            l[i],l[j] = l[j],l[i]
        else:
            pass
    l[i+1],l[pivot] = l[pivot],l[i+1]
    return i+1

def quick_sort(l,low,high):
    if low<high:
        par = Partition(l,low,high)
        quick_sort(l,low,par-1)
        quick_sort(l,par+1,high)
    print(l)
'''
def merge(l,low,mid,high):
    n = len(l)
    key=[]
    i,j,k=0,0,0
    
    while i<mid and j<mid:
        if l[i]<l[j]:
            key.append(l[i])
            i+=1
        else:
            key.append(l[j])
            j+=1

    while i< mid:
        key.append(i)
        i+=1
    while j< high:
        key.append(i)
        j+=1
        
    l[low:high] = key
def merge_sort(l):
    if len(l)>1:
        mid = len(l)//2
        low=l[:mid]
        high=l[mid:]
        merge_sort(low)
        merge_sort(high)
        merge(l,low,mid,high)
    print(l)
'''
def get_numb_digits(l):
    m = 0
    for item in l:
        m = max(item,m)
    return len(str(m))

from functools import reduce
def __flatten(A):
    return reduce(lambda x,y:x+y,A)

def radix(l,num_digits):
    for digits in range(0,num_digits):
        B = [[] for i in range(10)]
        for item in l:
            num =item//10 ** (digits)%10
            B[num].append(item)
        A=__flatten(B)
    return A

def counting(l):
    

l = list(map(int,input().split()))
bubble(l)
optim_bubble(l)
selection(l)
insertion(l)
quick_sort(l,0,len(l)-1)
n = get_numb_digits(l)
print(radix(l,n))
