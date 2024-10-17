class Missing(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class Duplicate(Exception):
    def __init__(self, message: str) -> None:
        self.message = message