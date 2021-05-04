import json
from os import path
class Quiz:
    """ Quizinator class demo concept """
    def __init__(self, data_path:str="data.json"):
        """ Load flash card data from local storage

        Parameter
        --------------
        data_path: str
            path to json file containing flash card data

        Return
        --------------
            None
        """
        if not path.exists(data_path): # If file does not exist exit
            raise FileNotFoundError

        self.quizinator = None
        with open(data_path, 'r') as f:
            self.quizinator = json.load(f)
