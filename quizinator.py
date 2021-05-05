# quizinator.py Beta version of the quizinator app
#
# Author: Team 3
# Date: April 30th, 2021
import json
from flashcard import FlashCard
from os import path

class Quiz:
    """ Beta version of the Quiz flash card app """
    def __init__(self, data_path:str = 'data.json') -> None:
        """ Load flash card data from local storage 
        
        Parameter
        ---------------
        data_path: str
            Path to local storage

        Return
        ---------------
        None
        """
        if not path.exists(data_path):
            raise FileNotFoundError

        self.path = data_path
        self.quizinator = {}
        with open(data_path, 'r') as f:
            self.quizinator = json.load(f)

        self._flashcard = [card for card in self.quizinator.keys()]

    def _get_input(self, question:str) -> str:
        """ Ensures user input is not empty
        
        Parameter
        ---------------
        prompt: str
            Prompt question for input function

        Return
        ---------------
        result: str
            Non empty user input
        """
        result = ''
        while result == '':
            result = input(question)
            if result == '':
                print("\n\tInvalid!!! Input can't be empty. Try Again\n")
        return result

    def _check_flashcard(self, term:str):
        """ Check if the flashcard already exists in the database or not 

        Parameter
        --------------
        term: str
            new flashcard term

        Return
        -------------
        found: bool
            True if flashcard exists in the database else False
        """
        return True if (term in self._flashcard) else False

    def add_flashcard(self) -> None:
        """ Add new flashcard into local json database
        
        Parameter
        ---------------
        prompt: None
        

        Return
        ---------------
        None
        """
        flashcard = FlashCard()
        term = self._get_input("Enter term for flashcard: ")
        while term in self._flashcard:
            print(f"Flashcard for <{term}> exists!")
            print(f'\t{term}: {self.quizinator[term]}')
            term = self._get_input("Enter term for flashcard: ")
        definition = self._get_input(f"Enter definition for {term}: ")
        flashcard.create_flashcard(term, definition)
        # Flashcard object will be left unused until we figure out how to implement the unique ID's
        self.quizinator[term] = {'definition': definition}
    
    def save_quizinator(self):
        """ Save current flashcards into(overight) local storage
        
        Parameter
        ---------------
        prompt: None
        

        Return
        ---------------
        None
        """
        with open(self.path, 'w') as fp:
            json.dump(self.quizinator, fp, indent=4)

if __name__ == '__main__':
    quiz = Quiz()
    quiz.add_flashcard()
    quiz.save_quizinator()

                    