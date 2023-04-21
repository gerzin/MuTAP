def move_one_ball(arr):
    
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True

def test():
    assert move_one_ball([1])==True
    assert move_one_ball([1,1,1])==True
    assert move_one_ball([1,2,3,2,2]) == True
    assert move_one_ball([2,2,2,2,1]) == True
    assert move_one_ball([3,3,3,3,3])==True
    assert move_one_ball([1,1,1,1,1]) == True
    assert move_one_ball([1,2,3,4]) == False
    assert move_one_ball([1,2,3,4,2]) == False
    assert move_one_ball([1,2,3,3,3]) == False
    
    
    
    
    
    
    
    
    
    
    
    
