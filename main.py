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
            print(f'All flashcards in this study set')
            quiz.view_flashcard()

        elif choice == 3:
            print('\nHere are your flahscards')
            quiz.view_flashcard() #replace with function to view all flashcards
            term = input('\nWhich flashcard would you like to update? (Please input the Term): ')
            quiz.edit_flashcard(term)

        elif choice == 4:
            print('Here are your flashcards:')
            quiz.view_flashcard()
            print()
            quiz.remove_flashcard()

        elif choice == 5:
            return False

if __name__  == '__main__':
    main()