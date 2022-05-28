import random

class Guesser:
    """The "Guesses" made by the user. 
    
    The responsibility of this class is to keep track of the input from the user, so we can compare it with the list of letters that we're using.
    
    Attributes:
        _guess: The single letter input by the user.

    """


    def __init__(self):
        """Constructs a new Guesser.
        
        Args:
          self (Guesser): An instance of Guesser.
        """
        self._guess = " "


    def get_guess(self):
        """Gets the current guess.
        
        Returns:
          letter: The current guess
        """
        return self._guess

    def update_guess(self, guess):
        """Updates the guess.
        
        Args:
          self (Guesser): An instance of Guesser.
          guess (str): The users guess."""
        self._guess = guess