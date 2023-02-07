# Binary Search
key=4
arr=[1,2,3,4,5,6]
l=len(arr)-1
f=0
flag=0
while(f<=l):
    mid=(f+l)//2
    if(key==arr[mid]):
        flag=1
        print("Found")
        break
    elif(key>arr[mid]):
        f=mid+1
    else:
        l=mid-1
print(flag)
