def floydwarshall(Wmat):
    (rows,cols,x) = Wmat.shape
    infinity = np.max(Wmat)*rows*rows+1
    SP = np.zeros((rows,cols,cols+1))
    for i in range(rows):
        for j in range(cols):
            SP[i,j,0] = infinity

    for i in range(rows):
        for j in range(cols):
            SP[i,j,0] = Wmat[i,j]

    for k in range(1,cols+1):
        for i in range(rows):
            for j in range(cols):
                SP[i,j,k] = min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])

    return(SP[:,:,cols])

