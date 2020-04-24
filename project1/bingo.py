import random
class Player:
    def __init__(self,table,playerId):
        self.table = table
        self.row = [0,0,0,0,0]
        self.column = [0,0,0,0,0]
        self.playerId = playerId
        
    def strikeNumber(self, choosen_number):
        row = self.row
        column = self.column
        for x in range(0,5):
            for y in range(0,5):
                if choosen_number == self.table[x][y]:
                    row[x] = row[x] + 1
                    column[y] = column[y] + 1
        score = row.count(5) + column.count(5)
        if score == 5:
            return [1,self.playerId]
        else:
            return [0]

class Game:
    def createPlayers(playersCount,defaultTable):
        players = []
        for y in range(0,playersCount):
            table = list(map(list, defaultTable))
            random.shuffle(table[0])
            random.shuffle(table[1])
            random.shuffle(table[2])
            random.shuffle(table[3])
            random.shuffle(table[4])
            players.append(Player(random.sample(table,5),y))
        return players

    def playGame(players):
        t = 0
        print("Enter the number to be striked with Player ID")
        while t < 10:
            userChoice = list(map(int,input().split()))
            for player in players:
                res = player.strikeNumber(userChoice[1]) 
                if res[0] == 1:
                    return res[1] + 1

class UserInterface:
    def startGame():
        print('Welcome to Bingo')
        n = int(input('Enter the no. of players ')) 
        table = []
        print("Enter the Numbers to be use in the game")
        for _ in range(0,5):
            table.append(list(map(int,input().split())))
        return n,table
        
    def displayWinner(playerId):
        print("Player {} is the winner".format(playerId))

def main():
    playersCount,table = UserInterface.startGame()
    players = Game.createPlayers(playersCount,table)
    winnerPlayerId = Game.playGame(players) 
    UserInterface.displayWinner(winnerPlayerId)
    
main()

