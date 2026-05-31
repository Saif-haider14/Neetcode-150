# Summary & Pattern to Remember 

you just have to perform `### 3 steps `  to solve this Problem .
# Step No 1 :
     Count the Frequency of every element in a list 
      used Dictionary for grouping element 

# Step No 2 :
     Sort the elemnts with their increasing count from left to right in increasing order 
     use (heap Queue) for that     
     import heapq
     heapq.heapify()
     heapq.heappop()
     heap usually works on list but if you apply on dictionary , it sort  only the keys and all the values are lost , but for our problem , we sort the keys according to the values , we have to sort the keys and values in such a way the  top frequent numbers are placed on the right side 
     and the least frequent values are on the left side


# Step No 3 :
      Find the top k Frequent values  by popping out all the values except top k frequent value


# Example :
    nums = [1 , 2 ,4, 6, 2 , 4 ,6 ,6]  , k = 1

    dictionary = {1 : 1 , 2 : 2 , 4 : 2 , 6: 3}
                  |    |
                 num : count

    converting to tuples so that heap can apply on it 

    heap = [(count , num) for num , count in dictionary.items()]

## count is replacing on key place beacuse we have to sort by counting/frequency of elements

    heapq.heapify(heap)     # Sorting the tuples it looks like :
   [ (1 , 1) , (2 , 2 ) ,( 2 ,4 ), (3 , 6)]

    for count , num in range(len(heap) - k):
            heapq.heappop(heap)                # output --->   [(3 ,6)]

    return [ num for count , num in heap]





