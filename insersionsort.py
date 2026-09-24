numbers = [3,84,20,98,55,7,15]

def insersion():
    for i in range(1,len(numbers)):
        num1 = numbers[i]
        j = i-1
        while j >= 0 and numbers[j] > num1:
            numbers[j+1] = numbers[j]
            j-=1
        numbers[j+1] = num1
        print(numbers)

insersion()