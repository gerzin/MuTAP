def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True
assert will_it_fly( [1,1,1,1], 5) == True
assert will_it_fly( [1,1,1,1,1], 5) == True
assert will_it_fly( [1,2], 5) == False 
