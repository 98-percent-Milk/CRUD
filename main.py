from quizinator import Quiz
from flashcard import FlashCard
from menu import Menu

def main():
    quiz = Quiz()
    flashcard = FlashCard()
    menu = Menu()

    while True:
        menu.display_menu
        choice = menu._get_choice_input

        if choice == 2:
            print(f'All flashcards in this study set')
            quiz.view_flashcard()

        elif choice == 3:
            print('\nHere are your flashcards') #replace with function to view all flashcards
            quiz.view_flashcard()
            key = input('\nWhich flashcard would you like to update? (Please input the ID): ')
            flashcard.edit_flashcard(quiz.quizinator, key)
            quiz.save_quizinator()

        elif choice == 4:
            print('here are your flashcards')
            for i in quiz.quizinator.values():
                print(i,end =" ")
            print()
            data = flashcard.remove_flashcard(quiz.quizinator)
            flashcard.save_to_json(data)

        elif choice == 5:
            return False

main()