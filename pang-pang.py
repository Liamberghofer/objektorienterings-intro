import random

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        hit = random.randint(1,5)
        if hit > 1:
            self.did_hit = True
       # Här sker "eldväxlingen"
        elif hit < 1:
            self.did_hit = False
        else:
            self.is_hitted = True

    def inc_scores(self):
        if self.did_hit == True:
            self.scores += 1
       # Här ska poängen öka

    def reduce_lifes(self):
        if self.is_hitted == True:
            self.lives -= 1
        # Här ska antalet liv minska


a_player = Player(3)       # Initiera en spelare med tre liv
a_player.fire()            # Spelaren skjuter