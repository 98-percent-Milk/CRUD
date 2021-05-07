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

        self._flashcard = [
            [k,self.quizinator[k]['term']] for k in self.quizinator.keys()
                            if isinstance(self.quizinator[k], dict)
                          ]
        
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

    def _check_flashcard(self, term:str) -> None:
        """ Check if the flashcard already exists in the database or not 
        If exists display Term and Definition on the screen
        Parameter
        --------------
        term: str
            new flashcard term

        Return
        -------------
        found: bool
            True if flashcard exists in the database else False
        """
        for x in self._flashcard:
            if term in x:
                print(f"Flashcard for <{term}> exists!")
                print(f"\n\t<{term.title()}>: {self.quizinator[x[0]]['def']}\n")
                return True
        return False

    def generate_id(self):
        """ Generates new unique id for the flashcard

        Parameter
        --------------
        None

        Return
        -------------
        new_id: str
            new unique id
        """
        new_id = ''
        if not self.quizinator['id'] == []:
            new_id = self.quizinator['id'].pop()
        else:
            new_id = str(len(self.quizinator))
        return new_id

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
        new_id = self.generate_id()
        term = self._get_input("Enter term for flashcard: ")

        while self._check_flashcard(term):
            term = self._get_input("Enter term for flashcard: ")

        definition = self._get_input(f"Enter definition for {term}: ")
        flashcard.create_flashcard(term, definition, new_id)
        self.quizinator[new_id] = flashcard.serialize()
    
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

    def edit_flashcard(self, key):
        """ Allows you to edit existing flashcards """
        # Check if the key exists in the database
        if key not in [x[1] for x in self._flashcard]:
            raise ValueError
        
        print(f"---Editing <{key}> flashcard---")
        for card in self._flashcard:
            if key == card[1]:
                fc_id = card[0] # getting flashcard unique id
                new_term = self._get_input('Please input new term: ')
                new_definition = self._get_input('Please input new definition: ')
                self.quizinator[fc_id]['term'] = new_term
                self.quizinator[fc_id]['def'] = new_definition
                break


if __name__ == '__main__':
    quiz = Quiz()
    # quiz.add_flashcard()
    # quiz.save_quizinator()
    quiz.edit_flashcard('html')
    quiz.save_quizinator()