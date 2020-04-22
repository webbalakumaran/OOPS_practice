import random
class Bingo:
    def __init__(self,table):
        self.table = table
        print(self.table, end=" cons")
        print()
    def display(self):
        print(self.table,end=" method" )
        print()

def get_table():
    temp = []
    for _ in range(0,5):
        temp.append(list(map(int,input().split())))
    return temp

def shuffle_table(table,n):
    objects = []
    for _ in range(0,n):
        print("loop")
        random.shuffle(table[0])
        random.shuffle(table[1])
        random.shuffle(table[2])
        random.shuffle(table[3])
        random.shuffle(table[4])
        objects.append(Bingo(random.sample(table,5)))
    return objects

def main():
    n = int(input())
    table = get_table()
    objects = shuffle_table(table,n)
    objects[0].display()
    objects[1].display()
main()