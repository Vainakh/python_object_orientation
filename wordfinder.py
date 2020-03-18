"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """reads text file with one word on one each line,
        can output a random word from file

        >>> wf = WordFinder("words.txt")
        3 words read

        >>> wf.make_word_list()
        ['cat', 'dog', 'porcupine']

        >>> wf.random()
        'cat'

        >>> wf.random()
        'cat'

        >>> wf.random()
        'porcupine'

        >>> wf.random()
        'dog'
     """

    def __init__(self, file):
        "takes in file(path) and stores in variable"
        self.file = file
        self.list = self.make_word_list() # Let's see if we need this

    def __refr__(self):
        return f"Instance of WordFinder for file @ {self.file}"

    def make_word_list(self):
        "reads file and creates list of words from the file"
        read_file = open(self.file, 'r')
        word_list = [line for line in read_file]
        # word_list = read_file.splitlist()
        # for word in word_list:
        #     # stripped = word.strip('\n')
        #     word.strip('\n')
        return word_list

    def random(self):
        "outputs random word from list"
        return choice(self.list).strip('\n')
        # use .random()


# wf.random()
#         #'cat'

# wf.random()
#         #'cat'

# wf.random()
#         #'porcupine'

# wf.random()
#         #'dog'


# # str.splitlines() - 
# Code #1

# # Python code to illustrate splitlines() 
# string = "Welcome everyone to\rthe world of Geeks\nGeeksforGeeks"
  
# # No parameters has been passed 
# print (string.splitlines( )) 
  
# # A specified number is passed 
# print (string.splitlines(0)) 
  
# # True has been passed  
# print (string.splitlines(True)) 
# Output :

# ['Welcome everyone to', 'the world of Geeks', 'GeeksforGeeks']
# ['Welcome everyone to', 'the world of Geeks', 'GeeksforGeeks']
# ['Welcome everyone to\r', 'the world of Geeks\n', 'GeeksforGeeks']
 