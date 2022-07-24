def sort_array(arr):
    ODD = sorted(list(filter(lambda x:x%2, arr)))
    res=[]
    k=0
    for i in range(len(arr)):
        if arr[i]%2:
            res.append(ODD[k])
            k+=1
        else:
            res.append(arr[i])
    return res
            
print(sort_array([5, 8, 6, 3, 4] )) # output --->  [3, 8, 6, 5, 4]