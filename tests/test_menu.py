import pytest
import mock
import builtins
from menu import Menu

@pytest.fixture(name='menu')
def fixture_menu():
    default = Menu()
    return default

def test_private_attributes(menu):
    """ Unit test for initializing menu class """
    assert menu._choice == ''
    assert menu._run == True

def test_get_choice_input_valid(menu):
    """ Unit test for valid user input """
    with mock.patch.object(builtins, 'input', side_effect=['1']):
        assert menu._get_choice_input == 1

def test_get_choice_input_invalid(menu):
    """ Unit test for invalid user input """
    with mock.patch.object(builtins, 'input', side_effect=[6, -1, 99, 1]):
        assert menu._get_choice_input == 1

def test_get_input_valueError(menu):
    """ Unit test for non integer type values """
    with mock.patch.object(builtins, 'input', side_effect=['1.2', 'potato', '1']):
        menu._get_choice_input