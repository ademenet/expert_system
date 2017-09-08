"""
This is the implementation of the backward chaining engine.
"""
class BackwardChaining(object):
    """Backward chaining engine.
    """
    def __init__(self, queries: list str, facts: list str, rules: list str):
        self.agenda = queries
        self.facts = facts
        self.rules = rules
        self.entailed = list()

    def execute(self) -> bool:
        if self.bcentails():
            pass
    
    def bcentails(self) -> bool:
        while len(self.agenda) > 0:
            # Take the first query
            query = self.agenda.remove()
            # Add it to entailed list
            self.entailed.append(query)
            # If this query is a fact, don't go further
            if query not in self.facts:
                symbols = list()
                for rule in self.rules:
                    # If the query appear in the conclusion, i.e. right part
                    if self.in_right(rule, query):
                        p = self.get_left(rule) # list str
                if len(p) == 0:
                    return False
                else:
                    for elem in p:                    
                        if elem not in self.entailed:
                            self.agenda.append(elem)
        return True


    def get_left(self, rule) -> list str:
        """Return the conjuncts of the left part."""
        pass

    def in_right(self, rule, query):
        """Check if query appear in the right part of the rule."""
        pass