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

        if choice == 3:
            print('\nHere are your flahscards\n', quiz.quizinator) #replace with function to view all flashcards
            key = input('Which flashcard would you like to update? ')
            flashcard.edit_flashcard(quiz.quizinator, key)
            quiz.save_quizinator()

        elif choice == 5:
            return False

main()