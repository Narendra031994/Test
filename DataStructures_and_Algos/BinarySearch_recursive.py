def BSearch(data,low,high,key):
    low = low
    high = high
    key = key
    mid = int((low+high)/2)
    if (low > high):
        print("No element found")
    else:
        if (key == data[mid]):
            return mid
        elif (key < data[mid]):
            return BSearch(data,low,mid-1,key)  
        else:
            return BSearch(data,mid+1,high,key)
data =[1,2,3,4]
high = len(data) - 1
low = 0
key = int(input("enter the key :"))
print(BSearch(data,low,high,key))


"""
Time complexity analysis:
1) Best case is when the element is at the first mid i.e O(1)
2) Worst case is when the element that we searching for is at the leaf node, where each node represent the mid value.
lets take a simple list and compute the mid values while searching for a key = 4:
list = [1,2,3,4], low = 0, high = len(list) - 1 = 3
1st iter : mid = 1 
second iter : mid = 2
third iter : mid = 3   "Element found here and it is at the leaf node"
Generalizing this, The worst case for binary search is height of the binary tree = logn
Using the big-oh notation i.e O(logn)
                                1
                               /\
                              0  2
                                  \
                                   3
"""
                                  



