class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket - player:{self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player}hits a six!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("score can not be negative")
class football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"football - player:{self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player}hits a six!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("score can not be negative")

    #create objects
cricket_player = Cricket("rohit", 85)
football_player = football("arjun",2)

print("===Sports scoreboards===\n")
for sport in (cricket_player, football_player):
    sport.info()
    sport.play()
    print()

print("---direct change attempt---")
cricket_player.__score = 999
print(f"get_score() still shows: {cricket_player.get_score()}")

print("n/---upadating scores---")
cricket_player.set_score(100)
football_player.set_score(3)