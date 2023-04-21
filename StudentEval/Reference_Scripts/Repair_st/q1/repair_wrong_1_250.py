def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    ref_counter = 0
    if ( len ( seq ) == 0 ) :
        position = 0
    for i in seq :
        if ( x <= i ) :
            position = i
        else :
            ref_counter += 1
    return ref_counter
