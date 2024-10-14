import random
def qsort(left, right):
    i,j=left,right
    x=random.randint(left,right)
    l[left],l[x]=l[x],l[left]
    k=l[left]
    while(i<j):
        while(i<j and int(l[j])>int(k)):
            j-=1
        if(i<j):
            l[i]=l[j]
            i+=1
        if(i>=j):break
        while(i<j and int(l[i])<int(k)):
            i+=1
        if(i<j):
            l[j]=l[i]
            j-=1
        if(i>=j):break
    l[i]=k
    if(i-1-left>=1 and left <=s and s<=i-1):qsort(left,i-1)
    if(right-i-1>=1 and i+1<=s and s<=right):qsort(i+1,right)
    if(s==i):return
    return
n,s=map(int,input().split())
l=input().split()
qsort(0,n-1)
print(l[s])