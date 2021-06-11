import doctest


class Borg:
    # name need __
    __origin_state = {}

    def __init__(self):
        # __origin_state need self
        self.__dict__ = self.__origin_state


class YourBorg(Borg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"

    def __repr__(self):
        return self.state


def main() -> None:
    """
    >>> inst0 = YourBorg()
    >>> inst1 = YourBorg()
    >>> inst0
    Init
    >>> inst0.state = "Idle"
    >>> inst1
    Idle
    >>> inst1.state = "Running"
    >>> inst2 = YourBorg("New Running")
    >>> inst0
    New Running
    """


if __name__ == "__main__":
    doctest.testmod()
