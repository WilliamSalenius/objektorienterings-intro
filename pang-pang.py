from random import randint

class Player():
    def __init__(self, lifes, scores):
        self.lifes = lifes
        self.scores = scores

    def fire(self):
        scope = randint(1, 5)
        if scope in {1, 2, 3}:
            self.did_hit = True
        else:
            self.did_hit = False

    def inc_scores(self):
        self.scores += 1
        
    def reduce_lifes(self):
        self.lifes -= 1

a_player = Player(3, 0)

while True:
    if a_player.lifes <= 0:
        break
    else:
        input('Tryck Enter för att skjuta')
        a_player.fire()
        if a_player.did_hit == True:
            print('Träff, du träffade!')
            a_player.inc_scores()
            print('Du klarade dig denna gång!')
            print(f"Dina poäng: {a_player.scores}")
            print(f"Dina liv: {a_player.lifes}")
        else:
            print('Miss, du blev skjuten!')
            a_player.reduce_lifes()
            print(f"Dina poäng {a_player.scores}")
            print(f"Dina liv {a_player.lifes}")