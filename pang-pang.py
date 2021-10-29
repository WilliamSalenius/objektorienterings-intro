from random import randint

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        scope = randint(1, 5)
        if scope in {1, 2, 3}:
            self.did_hit = True
            self.is_hittted = False
        else:
            self.did_hit = False
            self.is_hittted = True
       # Här sker "eldväxlingen"

    def inc_scores(self):
        if self.did_hit == True:
            self.scores += 1
        
       # Här ska poängen öka

    def reduce_lifes(self):
        if self.is_hitted == True:
            self.lifes -= 1
        
        # Här ska antalet liv minska

a_player = Player(3)       # Initiera en spelare med tre liv


while True:
    input('Tryck Enter för att skjuta')
    a_player.fire()
    if a_player.did_hit:
        print('Träff!')
        a_player.inc_scores() # Antalet poäng ökas med 1
    else:
        print('Miss, sikta bättre')
    if a_player.is_hitted == True:
        print('Aaaaaah')
        a_player.reduce_lifes() # Antalet liv minskas med 1
        print(f"Dina liv {a_player.lifes}")
        print(f"Dina poäng {a_player.scores}")
    else:
        a_player.inc_scores()
        print('Du klarade dig denna gång!')
        print(f"Dina poäng: {a_player.scores}")
        print(f"Dina liv: {a_player.lifes}")
    if a_player.lifes <= 0:
        break