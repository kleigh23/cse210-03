from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Parachute (Parachute): The game's Parachute.
        is_playing (boolean): Whether or not to keep playing.
        guesser (guesser): The game's guesser (the letter input).
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Retrieves the letter input by the user.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_letter("\nEnter a letter: ")
        self._guesser.update_guess(new_location)
        
    def _do_updates(self):
        """Take the input form the user, compare it to the list of letters we have.

        Args:
            self (Director): An instance of Director.
        """
        self._parachute.watch_guesser(self._guesser)
        
    def _do_outputs(self):
        """Based on the input from the user, it provides a drawing and a hint for the guesser to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._parachute.get_hint()
        self._terminal_service.write_text(hint)
        if self._parachute.is_found():
            self._is_playing = False
        #adding this last bit of code to avoid the game restarting automatically once the user loses
        if hint == "Got to restart!":
            self._is_playing = False