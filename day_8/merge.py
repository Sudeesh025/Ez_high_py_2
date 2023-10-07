def merge_sort(a):
    if(len(a)<=1):
        return a
    else:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while(i<len(left) & j<len(right)):
            if(left[i]<right[j]):
                a[k]=left[i]
                i=i+1
                k=k+1
            else:
                a[k]=right[j]
                j=j+1
                k=k+1
            while(i<len(left)):
                a[k]=left[i]
                i=i+1
                k=k+1
            while(j<len(right)):
                a[k]=right[j]
                j=j+1
                k=k+1
            print(a)
a=[8,2,3,4,5,6]
print(merge_sort(a))