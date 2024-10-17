from .init import conn, curs
from model.creature import Creature

curs.execute("""create table if not exists creature (
    name TEXT PRIMARY KEY,
    aka TEXT,
    country TEXT,
    area TEXT,
    description TEXT""")

def row_to_model(row: tuple) -> Creature:
    (name, description,country,  area, aka)  = row
    return Creature(name=name, description=description, aka=aka, area=area, country=country)

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump() if creature else None

def get_one(name: str) -> Creature | None:
    qry = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(creature: Creature) -> Creature:
    qry = """
    INSERT INTO creature (name, description, country, area, aka)
    VALUES (:name, :description, :country, :area, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(qry, params)
    conn.commit()
    return get_one(creature.name)

def modify(creature: Creature) -> Creature:
    qry = """
    UPDATE creature
    SET description=:description, country=:country, area=:area, aka=:aka
    WHERE name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature)

def delete(name: str) -> bool:
    qry = "DELETE FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    conn.commit()
    return True