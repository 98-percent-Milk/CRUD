import pytest
import mock
import builtins
from menu import Menu

def test_private_attributes():
    menu = Menu()
    assert menu._choice == ''
    assert menu._run == True

def test_display_menu(capfd):
    menu = Menu()
    menu.display_menu
    out, err = capfd.readouterr()
    assert out == ''.join([
        '\n{text:-^50}\n\n'.format(text='Quizinator Flash Card App'),
        "\t1. Practice\n",
        "\t2. View existing flash cards\n",
        "\t3. Update flash card\n",
        "\t4. Delete flash card\n",
        "\t5. Exit\n\n"
    ])

def test_get_choice_input_success():
    menu = Menu()
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert menu._get_choice_input == 1
