class Literal:
    name = ''
    value = False
    opposite = False

    def __init__(self, name):
        self.name = name

    def __init__(self, name, value):
        self.name = name
        self.value = value'

    def __init__(self, name, value, opposite):
        self.name = name
        self.value = value
        self.opposite = opposite

class Clause:
    clause = ''
    yieldValue = False
    literals = []

    def __init__(self, *args):
        
