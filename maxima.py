def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    eql_idx = -1;

    for i in range(len(x)):
        if i == 0:
            if x[i+1] < x[i]:
                idx.append( i )
            elif x[i+1] == x[i]:
                eql_idx = i
        elif i == len(x) - 1:
            if x[i-1] < x[i]:
                idx.append(i)
            elif x[i-1] == x[i]:
                if eql_idx < 0:
                    eql_idx = i
        # `i` is a local maximum if the signal decreases before and after it
        elif x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)


        elif x[i+1] == x[i]:
            if eql_idx < 0:
                eql_idx = i
        
        elif x[i+1] < x[i] and eql_idx > 0:
            for j in range( eql_idx, i + 1 ):
                idx.append( j )
            eql_idx = -1

        elif x[i+1] > x[i] and eql_idx > 0:
            eql_idx = -1
        
    if eql_idx > 0:
        for i in range( eql_idx, len(x)):
            idx.append( i )
    return idx
