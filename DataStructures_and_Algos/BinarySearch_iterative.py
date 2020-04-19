"""
BSearch is the function, it takes 2 params:
1) data : type list
2) key : type: int

it returns the index of the key in array
"""   
def BSearch(data,key):
    low = 0
    high = len(data)-1
    while (low<=high):
        mid = int((low+high)/2)
        if (key == data[mid]):
            return mid
        elif (key<data[mid]):
            high = mid-1
        else:
            low = mid+1
    return "Element not found"
result = BSearch([1,2,3,4],4)
print("Key found at index : ",result)      
        
    
         