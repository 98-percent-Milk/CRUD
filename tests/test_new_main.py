""" Unit test for main quiz class """
import pytest
import mock
import builtins
from main import main

def test_display_menu():
    """ Unit test for displaying the main menu """
    with mock.patch.object(builtins, 'input', side_effect=['7']):
        main()

def test_menu_option_one():
    """ Unit test for adding new flashcard into the database """
    with mock.patch.object(builtins, 'input', side_effect=['1', 'ruby', 'Ruby', 'computer language', '7']):
        main()

def test_menu_option_two():
    """ Unit test for viewing all the flashcards in the database """
    with mock.patch.object(builtins, 'input', side_effect=['2', '7']):
        main()

def test_menu_option_three():
    """ Unit test for editing existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['3','ruby', 'ruby', 'New Gem', '7']):
        main()

def test_menu_option_four():
    """ Unit test for deleting existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['4', '2', '7']):
        main()

def test_menu_option_five():
    """ Unit test for searching existing flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['5', 'python', '7']):
        main()

def test_menu_option_six():
    """ Unit test for searching learning flashcard """
    with mock.patch.object(builtins, 'input', side_effect=['6', 'y', '', 'n', 'n', '', 'e', '7']):
        main()