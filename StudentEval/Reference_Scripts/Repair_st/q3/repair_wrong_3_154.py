def remove_extras ( lst ) :
    result = [ ]
    for ele in lst :
        if ( ele not in result ) :
            result . append ( ele )
    return result
