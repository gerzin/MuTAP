def triangle_area(a, h):
    
    return a * h / 2.0





def test():
    assert triangle_area(10, 5) == 25
    assert triangle_area(5, 10) == 25
    assert triangle_area(3, 8) == 12.0
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(3, 5) == 7.5

