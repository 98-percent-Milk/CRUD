from controllers import Quiz
from views import Menu

class QuizController():
    """ Main function that runs the quizinator app """
    def __init__(self):
        self.quiz = Quiz()
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.display_menu
            choice = self.menu._get_choice_input

            if choice == 1:
                self.quiz.add_flashcard()
                print("\nFlashcard added.")

            elif choice == 2:
                self.menu.display_frame('All flashcards in this study set')
                self.quiz.view_flashcard()

            elif choice == 3:
                self.menu.display_frame('Here are your flashcards')
                self.quiz.view_flashcard()
                term = input('\nWhich flashcard would you like to update? (Please input the Term): ')
                self.quiz.edit_flashcard(term)
                print("Update saved.")

            elif choice == 4:
                self.menu.display_frame('Here are your flashcards:')
                self.quiz.view_flashcard()
                print()
                self.quiz.remove_flashcard()

            elif choice == 5:
                self.menu.display_frame('Searching for flashcard')
                terms = [x[1] for x in self.quiz._flashcard]
                print('\nTerms in your database: ')
                for i in terms: # may be remove this idk
                    print(i, end=", ")
                term =  input('\n\nWhich flashcard would you like to look at? (Please input the Term): ')
                self.quiz.search_flashcard(term)
                
            elif choice == 6:
                self.menu.display_frame('Learn your flashcards')
                self.quiz.learn()
                print()
                
            elif choice == 7:
                self.quiz.practice_flashcard()

            elif choice == 8:
                return False
