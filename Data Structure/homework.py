numbers = [20,30,50,60]
n=0
def addnumbers(num):
    if len(num) == 0:
        return 0
    total = num[0] + addnumbers(num[1:])
    print(total)
    return total

totalfunction = addnumbers(numbers)


