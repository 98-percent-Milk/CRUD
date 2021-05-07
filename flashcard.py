"""
flashcard.py Beta version of flash card for quizinator app
Author: Team 3
Date: April 30th
"""
import json
class FlashCard:
    """ Beta Flash Card class for quizinator app """
    def __init__(self):
        """ Initializes a new Flashcard """
        self.term = ''
        self.definition = ''
        self.id = ''


    def create_flashcard(self, term:str, definition:str, unique_id:str) -> None:
        """ Create new flashcard from user input

        Parameter
        --------------
        term: str
            Flashcard's term
        definition: str
            Definition of the flashcard's term
        unique_id: str
            Unique id for flashcard
        Return
        -------------
        None
        """
        if isinstance(term, str) and isinstance(definition, str) and isinstance(definition, str):
            if term == '' or definition == '':
                raise ValueError
            self.term = term
            self.definition = definition
            self.id = unique_id
        else:
            raise ValueError


    def serialize(self):
        return {
            'id': self.id,
            'term': self.term,
            'def': self.definition
        }


    def edit_flashcard(self, quiz_list, key):
        """ Allows you to edit existing flashcards """
        quiz = quiz_list

        if str(key) in quiz.keys():
            for items in quiz:
                if items == str(key):
                    print(f'\nCurrent flashcard:\nTerm: {quiz[items]["term"]}\nDef: {quiz[items]["def"]}')
                    term = input('\nPlease input new term: ')
                    definition = input('Please input new definition: ')
                    quiz[items]["term"] = term
                    quiz[items]["def"] = definition
                    print(f'\nUpdated flashcard:\nTerm: {quiz[items]["term"]}\nDef: {quiz[items]["def"]}')
                    # save to JSON
        else:
            return f'The flashcard with the given ID ({key}) does not exist.'


    def remove_flashcard(self,quiz_list):
        """ takes flashcard_id as input and deletes the corresponding flashcard"""
        quiz = quiz_list

        user_input  = input('Enter the flashcard id you want to remove ')
        while user_input not in quiz.keys():
            print('There is no flashcard', user_input)
            user_input = input('Re-enter the term you want to remove ')
        quiz.pop(user_input)
        print('the flashcard', user_input ,' has been deleted')
        dict1={}
        for i,j in quiz.items():
            if i.isdigit() == False:
                dict1[i] = j
            else:
                if int(i) < int(user_input):
                    dict1[i] = j
                else:
                    i = int(i)
                    i-=1
                    i = str(i)
                    dict1[i] = j
                    j['id'] = i
        return dict1


    def save_to_json(self,dict1):
        with open('data.json', 'w') as f:
            json.dump(dict1,f,indent = 4)

