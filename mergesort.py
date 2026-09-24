numbers = [3,84,20,98,55,7,15]

def mergesort(numlist):
    if len(numlist) <= 1:
        return numlist
    midpoint = len(numlist) // 2
    leftlist = numlist[0:midpoint] 
    rightlist = numlist[midpoint:]
    leftlist = mergesort(leftlist)
    rightlist = mergesort(rightlist)
    #mergeing the sorted list
    sortedlist = []
    i = 0
    j = 0
    while i < len(leftlist) and j < len(rightlist):
        if leftlist[i] > rightlist[j]:
            sortedlist.append(rightlist[j])
            j+=1
        else:
            sortedlist.append(leftlist[i])
            i+=1
    while i < len(leftlist):
        sortedlist.append(leftlist[i])
        i+=1
    while j < len(rightlist):
        sortedlist.append(rightlist[j])
    return sortedlist

sortlist = mergesort(numbers)
print(numbers)
print("")
print(sortlist)

