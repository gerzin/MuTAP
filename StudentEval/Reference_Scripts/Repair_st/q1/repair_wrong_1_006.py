def search ( x , lst1 ) :
    ref_lst = list ( lst1 )
    if ( len ( lst1 ) == 0 ) :
        if True :
            ref_lst . append ( x )
        elif ( x > lst1 [ ( length - 1 ) ] ) :
            pass
    else :
        pass
        for i in range ( len ( ref_lst ) ) :
            pass
            if ( x < ref_lst [ i ] ) :
                ref_lst . insert ( i , x )
            else :
                ref_lst . insert ( len ( ref_lst ) , x )
            pass
        pass
    pass
    for i in range ( len ( ref_lst ) ) :
        pass
        if ( ref_lst [ i ] == x ) :
            return i
        pass
    pass
