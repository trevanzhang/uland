from sqlite3 import IntegrityError
from .init import conn, curs
from model.explorer import Explorer
from error import Missing, Duplicate

curs.execute("""create table if not exists explorer (
    name TEXT PRIMARY KEY,
    country TEXT,
    description TEXT""")

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], description=row[2], country=row[1])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None

def get_one(name: str) -> Explorer | None:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"No explorer with name {name}")

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer) -> Explorer:
    qry = """
    INSERT INTO explorer (name, country, description)
    VALUES (:name, :country, :description)
    """
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except  IntegrityError:
        raise Duplicate(f"Explorer with name {explorer.name} already exists")   
    # conn.commit()
    return get_one(explorer.name)

def modify(explorer: Explorer) -> Explorer:
    qry = """
    UPDATE explorer
    SET description=:description, country=:country, name=:name
    WHERE name=:name_orig
    """
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    _ = curs.execute(qry, params)
    explorer2 = get_one(explorer.name)
    return explorer2

def delete(explorer: Explorer) -> bool:
    qry = "DELETE FROM explorer WHERE name=:name"
    params = {"name": explorer.name}
    res = curs.execute(qry, params)
    # conn.commit()
    return bool(res)