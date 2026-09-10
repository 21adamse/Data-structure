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

def sumdigitrecursion(num):
    if num == 0:
        return num 
    answer = num % 10 + sumdigitrecursion(num//10)
    print(answer)
    return answer
finalanswer= sumdigitrecursion(126)
print(finalanswer)

def palindromerecursion(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] != word[-1]:
        return False
    ispalindrome = palindromerecursion(word[1:-1])
    print(ispalindrome)
    return ispalindrome

ispalindrome = palindromerecursion("racecar")
if ispalindrome:
    print("That is a palindrome")
else:
    print("That isn't a palindrome")
 