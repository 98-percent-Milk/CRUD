""" Unit test for main quiz class """
import pytest
import mock
import builtins
from quizinator import Quiz

@pytest.fixture(name='quiz')
def fixture_quiz():
    default = Quiz()
    return default

def test_file_doesnt_exist():
    """ Unit test when file does not exists """
    with pytest.raises(FileNotFoundError):
        quiz = Quiz('datas.json')

def test_get_input(quiz, capfd):
    """ Unit test for valid user input """
    with mock.patch.object(builtins, 'input', side_effect=['', 'python']):
       assert quiz._get_input("Enter a term for flashcard: ") == 'python'

def test_add_fc(quiz):
    """ Unit test for adding new flashcard into database """
    with mock.patch.object(builtins, 'input', side_effect=['html/css', 'web interface']):
        quiz.add_flashcard()
        assert quiz.quizinator['2']['id'] == '2'   
        assert quiz.quizinator['2']['term'] == 'html/css'
        assert quiz.quizinator['2']['def'] == 'web interface'

def test_add_fc_again(quiz):
    """ Unit test for adding already existing fc into the database """
    with mock.patch.object(builtins, 'input', side_effect=['python', 'java', 'language']):
        quiz.add_flashcard()
        assert quiz.quizinator['3']['id'] == '3'
        assert quiz.quizinator['3']['term'] == 'java'
        assert quiz.quizinator['3']['def'] == 'language'

def test_check_fc(quiz):
    """ Unit test for checking if the flashcard already exists in the database """
    assert quiz._check_flashcard('python') == True

def test_remove_fc(quiz):
    """ Unit test for removing flashcard from the database """
    with mock.patch.object(builtins, 'input', side_effect=['4', '3']):
        quiz.remove_flashcard()

def test_view_fc(quiz):
    """ Unit test for displaying all the flashcard on display """
    quiz.view_flashcard()

def test_edit_fc_valueError(quiz):
    """ Unit test for Value Error while updating existing flashcard in database """
    with pytest.raises(ValueError):
        quiz.edit_flashcard('quiznos')

def test_edit_fc(quiz):
    """ Unit test for updating existing flashcard in database """
    with mock.patch.object(builtins, 'input', side_effect=['python', 'Main language']):
        quiz.edit_flashcard('python')

def test_generate_id(quiz):
    """ Unit test for generating unique id for flashcards """
    new_id = quiz.generate_id()
    assert new_id == '3'

def test_search_fc(quiz):
    """ Unit test for Value Error while searching existing flashcard in database """
    with pytest.raises(ValueError):
        quiz.search_flashcard('CSS')
        
def test_learn_show_all_fc(quiz):
    """ Unit test to display all the flashcard in the database """
    with mock.patch.object(builtins, 'input', side_effect=['y', 'no', '', 't', 'n', 'n', 'yes', '', 'e']):
        quiz.learn()

def test_learn_show_studied_fc(quiz):
    """ Unit test to display all the previously studied fc in db """
    inputs = ['y', '', 'n', 'n', '', 'b', 'y', '', 'b', 'y', '', 'b']
    with mock.patch.object(builtins, 'input', side_effect = inputs):
        quiz.learn()

def test_go_back_exit(quiz):
    """ Unit test for existing from go back function """
    inputs = ['y', '', 'n', '', 't', 'b', '', 'b']
    with mock.patch.object(builtins, 'input', side_effect = inputs):
        quiz.learn()

    inputs = ['n', '', 'n', '', 'b', '', 'n']
    with mock.patch.object(builtins, 'input', side_effect = inputs):
        quiz.learn()

    inputs = ['n', '', 'n', '', 'b', '', 't', 'e']
    with mock.patch.object(builtins, 'input', side_effect = inputs):
        quiz.learn()

def test_search(quiz):
    """ Unit test for searching fc in db """
    with pytest.raises(ValueError):
        quiz.search_flashcard('intresting')

    quiz.search_flashcard('python')

def test_continues_practice(quiz):
    """ Unit test for practice function """
    inputs = ['7', 'web interface', 'web interface']
    with mock.patch.object(builtins, 'input', side_effect=inputs):
        quiz.practice_flashcard()