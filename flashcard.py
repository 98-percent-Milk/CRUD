"""
falshcard.py Beta version of flash card for quizinator app
Author: Team 3
Date: April 30th
"""

class FlashCard:
    """ Beta Flash Card class for quizinator app """
    def __init__(self):
        """ Initializes a new Flashcard """
        self.term = ''
        self.definition = ''

    def create_flashcard(self, term:str, definition:str) -> None:
        """ Create new flashcard from user input

        Parameter
        --------------
        term:str
            Flashcard's term
        definition:str
            Definition of the flashcard's term

        Return
        -------------
        None
        """
        if isinstance(term, str) and isinstance(definition, str):
            if term == '' or definition == '':
                raise ValueError
            self.term = term
            self.definition = definition
        else:
            raise ValueError
