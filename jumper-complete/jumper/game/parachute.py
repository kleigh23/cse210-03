import random


class Parachute:
    """The drawing of the parachute man. 
    
    The responsibility of Parachute is to keep track of the drawing and messages being displayed. 
    
    Attributes:
        _location : We'll use this to have a choose a random word. Called "location" because it's the place were we're storing this word.
        _list_of_letter : The list of letters that compose the random word
        _word_completion : The amount of "completion" of the random word, we keep track of it with underscores (for ex: "ac__r" for "actor")
        _distance : The "distance" the parachute man picture has travelled! We'll use this to mark the "status" of the parachute man drawing and the message
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        wordlist = ["about", "above", "actor", "acute", "admit"]
        self._location = random.choice(wordlist)
        self._list_of_letter = list(self._location)
        self._word_completion = "_" * len(self._location)
        self._distance = 0
    
    def get_hint(self):
        """Writes the text prompt and displays the correct picture. We're storing the pictures as elements from a list.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            string: A hint for the user.
        """
        parachute_man =["""\

            --------
              __
            /____\\
            \    /
             \  /
              \/
               0
              /|\\
              / \\

            --------
            Five to go!
            """,

            """\

            --------
                
            /____\\
            \    /
             \  /
              \/
               0
              /|\\
              / \\

            --------
            Four to go!
            """,

            """\

            --------
                
                
            \    /
             \  /
              \/
               0
              /|\\
              / \\

            --------
            Three to go!
            """,

            """\

            --------
                
                
            \  /
             \/
              0
             /|\\
             / \\

            --------
            Two to go!
            """,

            """\

            --------
                
            \/
             0
            /|\\
            / \\

            --------
            ONE to go!
            """,

            """\

            --------
            
             x
            /|\\
            / \\

            --------
            Too bad!!
            """,

            "You did it!!!!"]

        hint = "Time to type something."
        if self._distance == 0:
            print(f"{parachute_man[0]}")
            print(self._word_completion)
            hint = "There's still 5 chances"
        elif self._distance == 1:
            print(f"{parachute_man[1]}")
            print(self._word_completion)
            hint = "There's still 4 chances"
        elif self._distance == 2:
            print(f"{parachute_man[2]}")
            print(self._word_completion)
            hint = "There's still 3 chances"
        elif self._distance == 3:
            print(f"{parachute_man[3]}")
            print(self._word_completion)
            hint = "There's still 2 chances"
        elif self._distance == 4:
            print(f"{parachute_man[4]}")
            print(self._word_completion)
            hint = "There's still 1 chances"
        elif self._distance == 5:
            print(f"{parachute_man[5]}")
            print(self._word_completion)
            hint = "Got to restart!"
        elif self._distance == 6:
            print(f"{parachute_man[6]}")
            print(self._word_completion)
            hint = "You won already!"
        return hint


    def is_found(self):
        """Whether or not the Parachute has been found.

        Here we mark if it's a success, and if so we don't update the status anymore.

        Args:
            self (Parachute): An instance of Parachute.
            
        Returns:
            boolean: True if the Parachute was found; false if otherwise.
        """
        if self._word_completion == self._location:
            print("you won the game!")
            return True
        
    def watch_guesser(self, guesser):
        """Here we mark if the letter that has been written by the user is useful or not.

        Args:
            self (Parachute): An instance of Parachute.
            guesser: The letter the user has "guessed"
        """
        if guesser.get_guess() in self._list_of_letter:
            word_as_list = list(self._word_completion)
            indices = [i for i, letter in enumerate(self._location) if letter == guesser.get_guess()]
            for index in indices:
                word_as_list[index] = guesser.get_guess()
            self._word_completion = "".join(word_as_list)
            print("Good guess!")
        else:
            print("nope")
            self._distance += 1
            
