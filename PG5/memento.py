class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def get_state(self):
        return self._state