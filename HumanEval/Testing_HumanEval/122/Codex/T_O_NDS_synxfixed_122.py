def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

def test():
    assert add_elements([1,6,0,0,0,6,7,8,9,0,0,6], 3) == 9
    assert add_elements([1,6,0,0,0,6,7,8,9,0,0,6], 4) == 12


test()
