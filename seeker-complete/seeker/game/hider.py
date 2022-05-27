import random

wordlist = ["about", "above", "actor", "acute", "admit"]
word_to_use = random.choice(wordlist)
list_of_letter = list(word_to_use)
list_for_distance = []




five_to_go =("""\

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
""")

four_to_go =("""\

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
""")

three_to_go = ("""\

--------
    
     
\    /
 \  /
  \/
  0
 /|\\
 / \\

--------
Three to go!
""")

two_to_go= ("""\

--------
     
     
 \  /
  \/
  0
 /|\\
 / \\

--------
Two to go!
""")

one_to_go= ("""\

--------
     
  \/
  0
 /|\\
 / \\

--------
ONE to go!
""")

fail_to_go = ("""\

--------
 
  x
 /|\\
 / \\

--------
Too bad!!
""")

success_to_go = ("You did it!!!!")

if list_for_distance(len)==0:
    stage = five_to_go
elif list_for_distance(len)==1:
    stage = four_to_go
elif list_for_distance(len)==2:
    stage = three_to_go
elif list_for_distance(len)==3:
    stage = two_to_go
elif list_for_distance(len)==4:
    stage = one_to_go
elif list_for_distance(len)==5:
    stage = fail_to_go
elif list_for_distance(len)>=10:
    stage = success_to_go

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
        self._distance = five_to_go
    
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
        if self._distance == five_to_go:
            hint = "There's still 5 chances"
        elif self._distance == four_to_go:
            hint = "There's still 4 chances"
        elif self._distance == three_to_go:
            hint = "There's still 3 chances"
        elif self._distance == two_to_go:
            hint = "There's still 2 chances"
        elif self._distance == one_to_go:
            hint = "There's still 1 chances"
        elif self._distance == fail_to_go:
            hint = "Got to restart!"
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
        return (self._distance== success_to_go)
        
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
        list_for_distance.append(1)


    
    #  def watch_seeker(self, seeker):
    #     """Watches the seeker by keeping track of how far away it is.

    #     Here we mark if the letter fits or not.


    #     Args:
    #         self (Hider): An instance of Hider.
    #     """
    #     distance = abs(self._location - seeker.get_location())
    #     self._distance.append(distance)   