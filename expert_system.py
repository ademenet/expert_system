"""
TODO: implement backward chaining inference engine.
"""
from collections import OrderedDict

class RulesList(object):
    """List of rules."""
    def __init__(self):
        self.rules_list = OrderedDict()

    def add(self):
        pass


class Fact(object):
    def __init__(self, letter: str, value: bool=False):
        self.letter = letter
        self.value = value


class Node(object):
    def __init__(self, value: str):
        self.left = None
        self.value = value
        self.right = None


class Rule(object):
    def __init__(self):
        self.left = left
        self.right = right
    
    def operate(self):
        if self.left:
            return self.right

    def backward(self):
        pass


class Graph(object):
    def __init__(self):
        self.graph = list()
    
    def push(self, left: str, right: str) -> None:
        node = dict()
        node = {left: right}
        self.graph.append(node)
    
    def pop(self):
        pass
    
    def display(self) -> None:
        print("{}".format(self.graph))

# class Facts(object):

class Queries(OrderedDict):
    def push(self, **kwargs):

        raise NotImplementedError

# FACTS en global
# RULES
def engine(query: str):
    if query in rules.right():

def main():
    pass

if __name__ == '__main__':
    # test = Graph()
    # test.push('A', '=>')
    # test.push('=>', 'B')
    # test.display()
    # gr = dict()
    # gr = {'A': ['&', 'C', '=>', 'B']
    #       'B': None}

    # t = Rule(left="1", right= "A")
    queries = OrderedDict()
    queries = {'A': None,
               'B': None,
               'C': None}

    facts = OrderedDict()
    facts = {'A': True,
             'B': False,
             'C': False}

    rules = [
        {'A': '=>',
         '=>': 'B'},
        {'A': '^',
         '^': 'B',
         'B': '=>',
         '=>': 'C'}
    ]

    print(queries)