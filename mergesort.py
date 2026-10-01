numbers = [3,84,20,98,55,7,15]

def mergesort(numlist):
    if len(numlist) <= 1:
        return numlist
    midpoint = len(numlist) // 2
    leftlist = numlist[0:midpoint] 
    rightlist = numlist[midpoint:]
    leftsorted = mergesort(leftlist)
    rightsorted = mergesort(rightlist)
    print("left",leftsorted)
    print("right",rightsorted)
    #mergeing the sorted list
    sortedlist = []
    i = 0
    j = 0
    while i < len(leftsorted) and j < len(rightsorted):
        if leftsorted[i] > rightsorted[j]:
            sortedlist.append(rightsorted[j])
            j+=1
        else:
            sortedlist.append(leftsorted[i])
            i+=1
    while i < len(leftsorted):
        sortedlist.append(leftsorted[i])
        i+=1
    while j < len(rightsorted):
        sortedlist.append(rightsorted[j])
        j+=1
    return sortedlist

sortlist = mergesort(numbers)
print(numbers)
print("")
print(sortlist)

