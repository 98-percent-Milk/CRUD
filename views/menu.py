# menu.py Beta version of Menu for quizinator app
#
# Author: Team 3
# Date: April 30th, 2021

class Menu:
    """ Menu for quizinator app """
    def __init__(self):
        """ Initializes menu class

        Parameter
        ----------------
        None

        Return
        ----------------
        Menu class object
        """
        self._choice = ''
        self._run = True
    
    @property
    def _get_choice_input(self) -> int:
        """ Get users menu choice input and check if the input is valid or not 
        
        Parameter
        ----------------
        None

        Return
        ----------------
        choice: int
            User's menu choice
        """
        choice = ''
        while type(choice) != int:
            try:
                choice = int(input("What would like to do: "))
                if choice > 8 or choice < 1:
                    print(f"\tSorry {choice} is not a valid menu option. Try again")
                    choice = ''
                    self.display_menu
            except ValueError as e:
                print("\tInvalid option!!! Please enter integer\n")
                self.display_menu
        
        return choice

    @property
    def display_menu(self) -> None:
        """ Display main menu of the quizinator flashcard app

        Parameter
        -----------------
        None

        Return
        ----------------
        None
        """
        print('\n{text:-^50}\n'.format(text='Quizinator FlashCard App'))
        print("\t1. Add flashcard")
        print("\t2. View existing flashcards")
        print("\t3. Update flashcard")
        print("\t4. Delete flashcard")
        print("\t5. Search flashcard")
        print("\t6. Learn flashcards")
        print("\t7. Practice flashcard")
        print("\t8. Exit\n")

    def display_frame(self, phrase) -> None:
        """ Display sentence/phrase/word in a nicer format

        Parameter
        -----------------
        None

        Return
        ----------------
        None
        """
        print('-' * 52)
        print('|', '{text:^48}'.format(text=phrase), '|')
        print('-' * 52)
