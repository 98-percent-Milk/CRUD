""" Unit test for main quiz class """
import pytest
import mock
import builtins
from controllers import QuizController

@pytest.fixture(name='main')
def fixture_main():
    default = QuizController()
    return default

def test_display_menu(main):
    """ Unit test for displaying the main menu """
    with mock.patch.object(builtins, 'input', side_effect=['8']):
        main.run()

def test_menu_option_one(main):
    """ Unit test for adding new flashcard into the database """
    with mock.patch.object(builtins, 'input', side_effect=['1', 'ruby', 'Ruby', 'computer language', '8']):
        main.run()

def test_menu_option_two(main):
    """ Unit test for viewing all the flashcards in the database """
    with mock.patch.object(builtins, 'input', side_effect=['2', '8']):
        main.run()

def test_menu_option_three(main):
    """ Unit test for editing existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['3','ruby', 'ruby', 'New Gem', '8']):
        main.run()

def test_menu_option_four(main):
    """ Unit test for deleting existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['4', '2', '8']):
        main.run()

def test_menu_option_five(main):
    """ Unit test for searching existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['5', 'python', '8']):
        main.run()

def test_menu_option_six(main):
    """ Unit test for searching learning flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['6', 'y', '', 'n', 'n', '', 'e', '8']):
        main.run()

def test_menu_option_seven(main):
    """ Unit test for practice function """
    with mock.patch.object(builtins, 'input', side_effect=['7', 'q', '8']):
        main.run()