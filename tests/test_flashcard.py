""" Unit test for flashcard class """
import pytest
import mock
import builtins
from models import FlashCard
from controllers import Quiz

@pytest.fixture(name='flashcard')
def fixture_flashcard():
    """ Default empty flashcard class """
    default = FlashCard()
    term = 'python'
    definition = 'programming language'
    unique_id = '123'
    default.create_flashcard(term, definition, unique_id)
    return default

def test_create_fc_valueError(flashcard):
    """ Test value error when creating flashcard """
    with pytest.raises(ValueError):
        flashcard.create_flashcard('python', 1, '123')

    with pytest.raises(ValueError):
        flashcard.create_flashcard(1.2, 'programming language', '')

    with pytest.raises(ValueError):
        flashcard.create_flashcard([1,2,3,4], {'apple': 'core'}, [])

    with pytest.raises(ValueError):
        flashcard.create_flashcard('', 'programming language', 23)

    with pytest.raises(ValueError):
        flashcard.create_flashcard('python', '', {})

    with pytest.raises(ValueError):
        flashcard.create_flashcard('', '', '')

        

def test_create_fc(flashcard):
    """ Test for creating flashcard """
    assert flashcard.term == 'python'
    assert flashcard.definition == 'programming language'
    assert flashcard.id == '123'

def test_serialization(flashcard):
    """ Test serialization of flashcard object into dictionary """
    assert flashcard.serialize() == {
        'id': '123',
        'term': 'python',
        'def': 'programming language'
    }

# tests for removing
def test_remove_fc(flashcard):
    pass