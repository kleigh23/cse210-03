import random

wordlist = ["about", "above", "actor", "acute", "admit"]
word_to_use = random.choice(wordlist)
list_of_letter = list(word_to_use)
tries = int(0)

parachute_man =[

"""\

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

"""\
YOU WIN!!!!
"""\
]


class Hider:
    """The drawing of the parachute man. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000). / ill use this to have a random word chosen
        _distance (List[int]): The distance from the seeker. / I'll use this to mark the "status" of the parachute man
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._location = word_to_use
        self._distance = parachute_man[tries]
    
    def get_hint(self):
        """Gets a hint for the seeker.
        
        Got to use this to mark the status! If you type a letter that fits, it should keep the current status (ex. five to go), if not it goes down one status (ex. four to go, and so on)
        Should this be done on director?

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        hint = "Time to type something."
        if self._distance == parachute_man[tries]:
            print(f"{parachute_man[0]}")
            hint = "There's still 5 chances"
        elif self._distance == parachute_man[1]:
            hint = "There's still 4 chances"
        elif self._distance ==parachute_man[2]:
            hint = "There's still 3 chances"
        elif self._distance == parachute_man[3]:
            hint = "There's still 2 chances"
        elif self._distance == parachute_man[4]:
            hint = "There's still 1 chances"
        elif self._distance == parachute_man[5]:
            hint = "Got to restart!"
        elif self._distance == parachute_man[6]:
            hint = "You won already!"
        return hint


    # def get_hint(self):
    #     """Gets a hint for the seeker.
     
 
    #     Args:
    #         self (Hider): An instance of Hider.
        
    #     Returns:
    #         string: A hint for the seeker.
    #     """
    #     hint = "(-.-) Nap time."
    #     if self._distance[-1] == 0:
    #         hint = "(;.;) You found me!"
    #     elif self._distance[-1] > self._distance[-2]:
    #         hint = "(^.^) Getting colder!"
    #     elif self._distance[-1] < self._distance[-2]:
    #         hint = "(>.<) Getting warmer!"
    #     return hint




    def is_found(self):
        """Whether or not the hider has been found.

        Here we mark if it's a success, and if so we don't update the status anymore.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        if self._distance == parachute_man[6]:
            return True
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Here we mark if the letter fits or not.


        Args:
            self (Hider): An instance of Hider.
        """
        if seeker in list_of_letter:
            print("Good guess!")
        else:
            print("nope")
            # tries+=1
            # return


    
    #  def watch_seeker(self, seeker):
    #     """Watches the seeker by keeping track of how far away it is.

    #     Here we mark if the letter fits or not.


    #     Args:
    #         self (Hider): An instance of Hider.
    #     """
    #     distance = abs(self._location - seeker.get_location())
    #     self._distance.append(distance)   