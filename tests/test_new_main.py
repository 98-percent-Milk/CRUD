""" Unit test for main quiz class """
import pytest
import mock
import builtins
from main import main

def test_display_menu():
    """ Unit test for displaying the main menu """
    with mock.patch.object(builtins, 'input', side_effect=['5']):
        main()

def test_menu_option_one():
    """ Unit test for choosing option one from menu """
    with mock.patch.object(builtins, 'input', side_effect=['1', 'ruby', 'Gem', '5']):
        main()

def test_menu_option_two():
    """ Unit test for choosing option two from menu """
    with mock.patch.object(builtins, 'input', side_effect=['2', '5']):
        main()

def test_menu_option_three():
    """ Unit test for choosing option three from menu """
    with mock.patch.object(builtins, 'input', side_effect=['3','ruby', 'ruby', 'New Gem', '5']):
        main()

def test_menu_option_four():
    """ Unit test for choosing option four from menu """
    with mock.patch.object(builtins, 'input', side_effect=['4', '2', '5']):
        main()