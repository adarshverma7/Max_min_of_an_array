def getminmax(arr):
    arr.sort()
    minmax={"min":arr[0],"max":arr[-1]}
    return minmax
arr=[10,4,2,5,6,0]
minmax=getminmax(arr)
print("minimum=",minmax["min"])
print("maximum=",minmax["max"])
