#! /usr/bin/env python3

class card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if(suit == "spades" or suit == "clubs"):
            self.color = "black"
        else:
            self.color = "red"

    
