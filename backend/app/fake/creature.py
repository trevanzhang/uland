from model.creature import Creature

def get_creatures():
    return [
        Creature(name="Bob", aka="Bobby", country="USA", area="New York", description="A friendly cat"),
        Creature(name="Mary", aka="Mary", country="USA", area="New York", description="A friendly dog"),
        Creature(name="Jim", aka="Jimmy", country="USA", area="New York", description="A friendly cat"),
    ]

_creatures = get_creatures()

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature:
    for creature in _creatures:
        if creature.name == name:
            return creature

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(name: str):
    return None