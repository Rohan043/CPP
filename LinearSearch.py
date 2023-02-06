# Linear Search
arr=[1,2,3,4,5,6]
b=4 #b=int(3.5) or b=8 or b=3.5
flag=0
for i in range(len(arr)):
    if arr[i]==b:
        print("element found")
        #print(i) *for index value
        flag=1
        break
    if flag==0:
        print("Not Found")
