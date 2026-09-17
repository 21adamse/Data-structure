

def binarysearch(datalist,value):
    midpointvalue = 0
    lb = 0
    ub = len(datalist)-1
    found = False
    while value != midpointvalue and ub > lb:
        midpoint = (ub + lb) // 2
        midpointvalue = datalist[midpoint]
        if midpointvalue < value and midpoint > 0:
            lb = midpoint+1
        elif midpointvalue > value and midpoint < len(datalist):
            ub = midpoint-1
        else:
            found = True
            print(str(value),"found at point",str(midpoint))
    if not found:
        print("Value not in list")
            
binarysearch([22,25,30,56,75,99],40)

    