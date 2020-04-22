import random
class Bingo:
    def __init__(self,table,player_id):
        self.table = table
        self.row = [0,0,0,0,0]
        self.column = [0,0,0,0,0]
        self.player_id = player_id
        # print(self.table)
        
    def play_game(self, choosen_number):
        # print(self.table)
        row = self.row
        column = self.column
        for x in range(0,5):
            for y in range(0,5):
                if choosen_number == self.table[x][y]:
                    print("Striked number")
                    row[x] = row[x] + 1
                    column[y] = column[y] + 1
        score = row.count(5) + column.count(5)
        # print(row,column)
        # print(score)
        if score == 5:
            return [1,self.player_id]
        else:
            return [0]

def get_table():
    temp = []
    for _ in range(0,5):
        temp.append(list(map(int,input().split())))
    return temp

def shuffle_table(table_param,n):
    objects = []
    for y in range(0,n):
        table = list(map(list, table_param))
        random.shuffle(table[0])
        random.shuffle(table[1])
        random.shuffle(table[2])
        random.shuffle(table[3])
        random.shuffle(table[4])
        objects.append(Bingo(random.sample(table,5),y))
        # print("Numbers for player {0}".format(y))
        # print(table)
    return objects

def main():
    n = int(input('Enter the no. of players '))
    table = get_table()
    objects = shuffle_table(table,n)
    t = 0
    end = 0 
    while t < 10 and end == 0:
        # print("playing")
        user_choice = list(map(int,input().split()))
        player_id = user_choice[0] - 1
        for x in objects:
            res = x.play_game(user_choice[1]) 
            if res[0] == 1:
                print("Player {} is the winner".format(res[1]))
                end = 1
                break
main()