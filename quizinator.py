# quizinator.py Beta version of the quizinator app
#
# Author: Team 3
# Date: April 30th, 2021
import json
from web_version.the_app.route.fc import practice
from menu import Menu
from flashcard import FlashCard
from os import path
import random

menu = Menu()

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

    def search_flashcard(self, term):
        if term not in [x[1] for x in self._flashcard]:
            raise ValueError
        else:
            for i in self._flashcard:
                if term == i[1]:
                    fc_id = i[0]
                    print('term :',term)
                    print('defination :',self.quizinator[fc_id]["def"])


    def practice(self):
        list_of_IDS = [x for x in self.quizinator if x != 'id']
        studied_cards = []
        """number of items in the dictionary"""
        user_study_choice = ''
        while user_study_choice not in ['y', 'n']:
            user_study_choice = input("Would you like to see the terms first if No the definition will be displayed first. Y/N\n").lower()
        side = True if user_study_choice == 'y' else False

        while len(list_of_IDS) != 0:
            
            random_card = random.choice(list_of_IDS)
            """makes sure that when studying there are no repeated cards"""
            test_term = self.quizinator[random_card]['term']
            test_def = self.quizinator[random_card]['def']

            # adding current flash card into studied cards
            list_of_IDS.remove(random_card)
            """if the user enters 'Y/y' the term will be printed first"""
            self.display_card(side, test_term, test_def)
            
            """options to view the next card or previous"""
            while True:
                user_option = input("Select an option: N(ext), B(ack), E(xit): ").lower()
                if (user_option == 'n'):
                    break
                elif (user_option == 'b'):
                    while True:
                        print(studied_cards)
                        if self.go_back(studied_cards, side):
                            menu.display_frame("Continuing with study")
                            break
                    break
                elif (user_option == 'e'):
                    break
                else:
                    print("Please input a valid option argument.")

            studied_cards.append(random_card)
        if len(list_of_IDS) == 0:
            print("\nGoodjob you've went through all the flashcards.")


    def go_back(self, studied_cards, side):
        menu.display_frame("Previous Flashcards")
        try:
            old_card = studied_cards.pop()
            test_term = self.quizinator[old_card]['term']
            test_def = self.quizinator[old_card]['def']
        except IndexError:
            print("\nNo more previously studied card\n")
            return True

        while True:
            self.display_card(side, test_term, test_def)
            while True:
                user_study_choice = input("What would you like to do: N(ext), B(ack), E(xit): ").lower()
                if user_study_choice == 'e':
                    return True
                elif user_study_choice == 'n':
                    return True
                elif user_study_choice == 'b':
                    return False
                else:
                    print("Please input a valid option argument.")

    def search_flashcard(self, term):
        if term not in [x[1] for x in self._flashcard]:
            raise ValueError
        else:
            for i in self._flashcard:
                if term == i[1]:
                    fc_id = i[0]
                    print('term :',term)
                    print('defination :',self.quizinator[fc_id]["def"])
    
    def display_card(self, side: bool, test_term: str, test_def:str):
        first = "Term" if side else "Definition"
        second = "Definition" if first == 'Term' else "Term"
        print(f"{first}:\n\t{test_term if first == 'Term' else test_def}\n")
        while input('press Enter to see the other side of the card: ') != '':
            pass
        print(f"\n{second}:\n\t{test_def if second == 'Definition' else test_term}\n")


    def practice_flashcard(self):
        """ A function to practice existing flashcards and get score"""
        lst =[]
        ans = ""
        score =0
        while ans!= 'q':
            id_lst =   [x[0] for x in self._flashcard]
            length = len(id_lst)
            ran_num = random.randint(0, length -1 )
            while ran_num not in lst:
                ran_term = id_lst[ran_num]
                print('Term: ' ,self.quizinator[str(ran_term)]['term'])
                ans = input('Enter defination or q to quit: ')
                if ans.lower()== self.quizinator[str(ran_term)]['def'].lower():
                    score+=1
                lst.append(ran_num)
                if len(lst)  == len(id_lst):
                    print('----------Your score------------')
                    print('You scored ', score,'out of', length)
                    ans ='q'
                    break
            
    

    