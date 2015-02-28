from random import randint
import Shoe

class Dealer(Shoe.Shoe):
    """A dealer who handles the <Shoe> and dealing out <Player>s"""
    def __init__(self, size=1, avatar="scambot", hit="soft", payout=3/2):
        """Initializes dealer avatar, deck size, black jack payout, and whether he
            hits or stays on a soft 17"""
        self.size=size
        self.avatar=avatar
        self.hit=hit
        self.payout=payout
        self.card_list=[]
        self.build_shoe()
        self.game_deck=self.shuffle(self.card_list)
    def shuffle(self, shuffle_this=[]):
        """Shuffles any list it is given, returns shuffled list"""
        self.shuffle_this=shuffle_this
        self.temp_list=[]
        for i in reversed(range(len(self.shuffle_this))):
            x=randint(0,len(self.shuffle_this)-1)
            self.temp_list.append(self.shuffle_this[x])
            del self.shuffle_this[x]
        return self.temp_list
