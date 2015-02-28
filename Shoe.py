class Card:
    """Cards in blackjack have a value, a name, and a suit"""
    def __init__(self, name="", suit="", value=0):
        """Initializes a new card that has a name, a suit, and a value."""
        self.name=name
        self.suit=suit
        self.value=value

class Shoe:
    """A blackjack shoe is typically 1 to 6 decks of 52 cards"""
    def __init__(self, size=1, back="royal", front="royal"):
        """The default decksize is one. Royal is a placeholder value for
           possible graphical changes"""
        self.size=size
        self.back=back
        self.front=front
    def build_suit(self, suit=""):
        """Builds A-K in a given suit and appends it to the card list"""
        self.suit=suit
        for i in range(0,13):
            if(i+1==1):
                self.card_list.append(Card("A",self.suit,(1,11)))
            elif(i+1>=1 and i+1<=10):
                self.card_list.append(Card(i+1,self.suit,i+1))
            elif(i+1==11):
                self.card_list.append(Card("J",self.suit,10))
            elif(i+1==12):
                self.card_list.append(Card("Q",self.suit,10))
            else:
                self.card_list.append(Card("K",self.suit,10))
    def build_deck(self):
        """Builds a deck of 4 suits"""
        self.build_suit("Spades")
        self.build_suit("Clubs")
        self.build_suit("Diamonds")
        self.build_suit("Hearts")
                
    def build_shoe(self):
        """Builds a shoe out of a <size> of decks. Each deck is 52<Card>s,
           these cards are put into one list, and then a shuffled list."""
        #The shoe is built out of <size> decks, each with 52 initializations
        #of the <Card> object. For loop doesn't work for 1 deck.
        if(self.size==1):
            self.build_deck()
        else:
            for i in range(0,self.size):
                self.build_deck()
            
            
