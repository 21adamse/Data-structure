class Reversestack():
    def __init__(self,word):
        self.list = []
        for letter in word:
            self.list.append(letter)
    def reverseword(self):
        while len(self.list) > 0:
            print(self.list.pop(), end= "")

reverseword = Reversestack("hello")
reverseword.reverseword()
