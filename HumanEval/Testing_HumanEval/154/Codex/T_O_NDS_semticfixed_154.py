def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False


def test():
    assert cycpattern_check("abcd","cdab") == True
    assert cycpattern_check("abcd","cdac") == False
    assert cycpattern_check("abcd","cbad") == False
