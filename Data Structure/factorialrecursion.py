factorialnum = int(input("Enter the factorial you want to calculate"))

def factorial(num):
    if num == 1 or num == 0:
        return num
    factor = num * factorial(num-1)
    print(factor)
    return factor

finalnum = factorial(factorialnum)

def wordrecursion(newword):
    if len(newword) == 0:
        return newword
    newword = newword[-1] + wordrecursion(newword[0:-1:])
    print(newword)
    return newword
finalword = wordrecursion("python")
print(finalword)

def digitrecursion(num):
    if num == 0:
        return num 
    answer = num % 10 + digitrecursion(num//10)
    print(answer)
    return answer
finalanswer= digitrecursion(126)
print(finalanswer)
