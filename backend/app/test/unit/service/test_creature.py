from model.creature import Creature
from service import creature as code

sample = Creature(name="Sample", aka="Sample", area="Sample", country="Sample", description="Sample")

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("sample")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("not_a_creature")
    assert resp is None