from model.explorer import Explorer

_explorers = [
    Explorer(name="Jane Doe",
             country="USA",
             description="Jane is a US citizen and has been to Mars."),
    Explorer(name="John Smith",
             country="UK",
             description="John is a UK citizen and has been to Mars."),
]

def get_all() -> list[Explorer]:
    """Get all explorers"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """Add a new explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Paitially modify an existing explorer"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Replace an existing explorer"""
    return explorer

def delete(name: str) -> bool:
    return None
