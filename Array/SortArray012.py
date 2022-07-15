
#Input: 
#N = 5
#arr[]= {0 2 1 2 0}
#Output:
#0 0 1 2 2
#Explanation:
#0s 1s and 2s are segregated 
#into ascending order.
# method 01:

def sort012(arr,n): # n = size of arr
    nextZero = 0
    nextTwo = n-1
    i = 0
    while i<=nextTwo:
        if arr[i]==0:
            arr[nextZero],arr[i] = arr[i],arr[nextZero]
            nextZero+=1
            i+=1
        elif arr[i]==2:
            arr[nextTwo],arr[i] = arr[i],arr[nextTwo]
            nextTwo-=1
        else:
            i+=1
    return arr

#method 02: I did create a new array here :( 
arr =[0,1,0,2,2,1]

x = arr.count(0)
y = arr.count(1)
z = arr.count(2)
i=0
while x>0:
    arr[i]=0
    i+=1
    x-=1

while y>0:
    arr[i]=1
    i+=1
    y-=1
    
while z>0:
    arr[i]=2
    i+=1
    z-=1
    
print(arr)
