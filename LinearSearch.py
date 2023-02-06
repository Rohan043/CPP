# Linear Search
arr=[1,2,3,4,5,6]
b=4
flag=0
for i in range(len(arr)):
    if arr[i]==b:
        print("element found")
        flag=1
        break
    if flag==0:
        print("Not Found")
