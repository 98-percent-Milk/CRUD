"""
flashcard.py Beta version of flash card for quizinator app
Author: Team 3
Date: April 30th
"""

# from quizinator import Quiz

class FlashCard:
    """ Beta Flash Card class for quizinator app """
    def __init__(self):
        """ Initializes a new Flashcard """
        self.term = ''
        self.definition = ''
        self.id = ''

    def create_flashcard(self, term:str, definition:str, new_id) -> None:
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
            self.id = new_id
        else:
            raise ValueError


    def edit_flashcard(self, quiz_list, key):
        """ Allows you to edit existing flashcards """
        quiz = quiz_list

        if str(key) in quiz.keys():
            for items in quiz:
                if items == str(key):
                    print(f'Current flashcard: {quiz[items]}')
                    term = input('Please input new term: ')
                    definition = input('Please input new definition: ')
                    quiz[items]["term"] = term
                    quiz[items]["def"] = definition
                    print(f'Updated flashcard: {quiz[items]}')
                    # serialize and save to JSON
        else:
            print(f'The flashcard with the given ID ({key}) does not exist.')