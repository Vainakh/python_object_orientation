"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Creating counter with a default value"
        self.start = start
        self.counter = start - 1

    def __repr__(self):
        return f"< Instance of SerialGenerator.  start = {self.start} counter = {self.counter} >"

    def generate(self):
        self.counter += 1
        return self.counter

    def reset(self):
        self.counter = self.start - 1

    
