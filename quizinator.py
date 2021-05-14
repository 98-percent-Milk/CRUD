# quizinator.py Beta version of the quizinator app
#
# Author: Team 3
# Date: April 30th, 2021
import json
from web_version.the_app.route.fc import practice
from flashcard import FlashCard
from os import path
import random

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
        None
        
        Return
        ---------------
        None
        """
        flashcard = FlashCard()
        new_id = self.generate_id()
        term = self._get_input("Enter term for flashcard: ")

        while self._check_flashcard(term):
            term = self._get_input("Enter term for flashcard: ")
        self._flashcard.append([new_id, term])
        definition = self._get_input(f"Enter definition for {term}: ")
        flashcard.create_flashcard(term, definition, new_id)
        self.quizinator[new_id] = flashcard.serialize()
        self.save_quizinator()

    def save_quizinator(self):
        """ Save current flashcards into(overight) local storage
        
        Parameter
        ---------------
        None
        
        Return
        ---------------
        None
        """
        with open(self.path, 'w') as fp:
            json.dump(self.quizinator, fp, indent=4)

    def edit_flashcard(self, key:str) -> None:
        """ Allows you to edit existing flashcards 
        
        Parameter
        ---------------
        key: str
            Flashcard term
        
        Return
        ---------------
        None
        """
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
        self.save_quizinator()


    def view_flashcard(self) -> None:
        """Prints all the flashcards with term the then definition on the next line.
        
        Parameter
        ---------------
        None
        
        Return
        ---------------
        None
        """
        for flashcard in self.quizinator:
            if flashcard != "id":
                print(f'Term: {self.quizinator[flashcard]["term"]}\nDefinition:{self.quizinator[flashcard]["def"]}')

    def remove_flashcard(self) -> None:
        """ takes flashcard_id as input and deletes the coressponding flashcard
       
        Parameter
        ---------------
        None
        
        Return
        ---------------
        None
        """
        user_input  = input('Enter the flashcard id you want to remove: ')
        while user_input not in self.quizinator.keys():
            print('There is no flashcard', user_input)
            user_input = input('Re-enter the term you want to remove: ')
        self.quizinator.pop(user_input)
        print('the flashcard', user_input ,' has been deleted')
        self.quizinator['id'].append(user_input)
        self.save_quizinator()

    def practice(self):
        list_of_IDS = [x for x in self.quizinator if x != 'id']
        print(list_of_IDS)
        if len(list_of_IDS) == 0:
            print("There are no flashcards in the current study set. Please create some to practice.")
        studied_cards = []
        """number of items in the dictionary"""


        

        while True:
            user_study_choice = input("Would you like to see the terms first if No the definition will be displayed first. Y/N\n")
            random_card = random.choice(list_of_IDS)
            """makes sure that when studying there are no repeated cards"""
            test_term = self.quizinator[random_card]['term']
            test_def = self.quizinator[random_card]['def']

            # adding current flash card into studied cards
            studied_cards.append(list_of_IDS.pop(int(random_card) - 1))
            """if the user enters 'Y/y' the term will be printed first"""
            if (user_study_choice in ['y', 'Y']):
                print(f"Term:\n{test_term}\n")
                # print(f"Term:\n{self.quizinator[str(random_card)]['term']}\n")

                # list_of_IDS.pop(list_of_IDS.index(random_card))
                flipcard = input("press Enter to see the other side of the card: ")

                """prints the rest of the flashcard when the user presses 'Enter'"""
                while flipcard != "":
                    flipcard= input("---press Enter to proceed---")

                if flipcard == "":
                    print(f"Term:\n\t{test_term}\n")
                    print()
                    print(f"Definition:\n\t{test_def}\n")
            # if the user enters N/n the definition will be printed first
            elif (user_study_choice in ['n', 'N']):
                print(f"Definition:\n\t{test_def}\n")

                """prints the rest of the flashcard when the user presses 'Enter'"""
                flipcard = input("---press Enter to see the other side of the card---")
                while flipcard != "":
                    flipcard= input("---press Enter to proceed---")
                if flipcard == "":
                    print(f"Term:\n\t{test_term}\n")
                    print()
                    print(f"Definition:\n\t{test_def}\n")
            
            """options to view the next card or previous"""
            User_option = input("Select an option: N(ext), B(ack), E(xit): ")
            if (User_option in ['n', 'N']):
                continue
            elif (User_option in ['b', 'B']):
                print(studied_cards)
                if len(studied_cards) == 0:
                    print("There is no previous card to study.")
                    continue
                else:
                    self.practice_helper(studied_cards)
            elif (User_option in ['e', 'E']):
                break
            elif len(list_of_IDS) == 0:
                break
            else:
                raise ValueError("Please input a valid option argument.")

    def practice_helper(self, studied_cards):
        old_card = studied_cards.pop()
        test_term = self.quizinator[old_card]['term']
        test_def = self.quizinator[old_card]['def']
        user_study_choice = input("Would you like to see the terms first if No the definition will be displayed first. Y/N\n")
        """makes sure that when studying there are no repeated cards"""
        if (user_study_choice in ['y', 'Y']):
            print(f"Term:\n{test_term}\n")
            # print(f"Term:\n{self.quizinator[str(random_card)]['term']}\n")

            # list_of_IDS.pop(list_of_IDS.index(random_card))
            flipcard = input("press Enter to see the other side of the card: ")

            """prints the rest of the flashcard when the user presses 'Enter'"""
            while flipcard != "":
                flipcard= input("---press Enter to proceed---")

            if flipcard == "":
                print(f"Term:\n\t{test_term}\n")
                print()
                print(f"Definition:\n\t{test_def}\n")
        # if the user enters N/n the definition will be printed first
        elif (user_study_choice in ['n', 'N']):
            print(f"Definition:\n\t{test_def}\n")

            """prints the rest of the flashcard when the user presses 'Enter'"""
            flipcard = input("---press Enter to see the other side of the card---")
            while flipcard != "":
                flipcard= input("---press Enter to proceed---")
            if flipcard == "":
                print(f"Term:\n\t{test_term}\n")
                print()
                print(f"Definition:\n\t{test_def}\n")
