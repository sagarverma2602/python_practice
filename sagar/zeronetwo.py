a=[2,0,1]
i=0
j=0
k=len(a)-1
n=0
while j<=k:
    if a[j]==0:
        a[i],a[j]=a[j],a[i]
        i+=1
        j+=1
    elif a[j]==1:
        j+=1
    else:
        a[j],a[k]=a[k],a[j]
        
        k-=1
    n+=1
print(a)
