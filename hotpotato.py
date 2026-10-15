class Hotpotato():
    def __init__(self):
        self.list = []
    def enterplayers(self,numplayers):
        for i in range(numplayers):
            playername = input("Enter player name")
            self.list.append(playername)
    def playgame(self):
        while len(self.list) > 1:
            for i in range(2):
                movedvalue = self.list[0]
                self.list.remove(self.list[0])
                self.list.append(movedvalue)
            eliminated = self.list[0]
            print(eliminated,"was eliminated")
            self.list.remove(self.list[0])
        print(self.list[0],"won")

game = Hotpotato()
game.enterplayers(4)
game.playgame()