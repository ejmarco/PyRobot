def binarySearch(alist,item):  
    first = 0
    last = alist.count - 1
    found = False
    while first <= last and not found:
        midpoint = (first+last)/2
        if alist[midpoint] == item:
            found = True
        else:
            if item > alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    if found == True:
        chain = "Trobat a la posicio: " + str(midpoint)
    else:
        chain = "Element no trobat"
    return chain
