def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


assert pairs_sum_to_zero([-1, -2, -7, -8, -9, -2]) == False
