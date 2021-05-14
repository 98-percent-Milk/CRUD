from quizinator import Quiz
from menu import Menu

def main() -> None:
    """ Main function that runs the quizinator app """
    quiz = Quiz()
    menu = Menu()

    while True:
        menu.display_menu
        choice = menu._get_choice_input

        if choice == 1:
            quiz.add_flashcard()

        elif choice == 2:
            menu.display_frame('All flashcards in this study set')
            quiz.view_flashcard()

        elif choice == 3:
            # print('\nHere are your flashcards')
            menu.display_frame('Here are your flashcards')
            quiz.view_flashcard() #replace with function to view all flashcards
            term = input('\nWhich flashcard would you like to update? (Please input the Term): ')
            quiz.edit_flashcard(term)

        elif choice == 4:
            menu.display_frame('Here are your flashcards:')
            quiz.view_flashcard()
            print()
            quiz.remove_flashcard()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> db0b89af6895ee486b5b7029cebb5d167e22476f

        elif choice == 5:
            menu.display_frame('Searching for flashcard')
            terms = [x[1] for x in quiz._flashcard]
            print('\nHere are your terms: ')
            for i in terms: # may be remove this idk
                print(i, end=", ")
            term =  input('\n\nWhich flashcard would you like to search? (Please input the Term): ')
            quiz.search_flashcard(term)
<<<<<<< HEAD

        elif choice == 6:
=======
=======
>>>>>>> db0b89af6895ee486b5b7029cebb5d167e22476f
            
        elif choice == 6:
            menu.display_frame('Practice')
            quiz.practice()
            print()
            
        elif choice == 7:
<<<<<<< HEAD
>>>>>>> c9d8f84eb6729381574a87cd64f56214e0ce1802
=======
>>>>>>> db0b89af6895ee486b5b7029cebb5d167e22476f
            return False

if __name__  == '__main__':
    main()