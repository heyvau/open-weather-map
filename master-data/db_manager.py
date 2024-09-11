import sqlalchemy as db
from sqlalchemy.sql import text
from logger import log


class DBManager:
    def __init__(self, engine: str) -> None:
        self.engine = db.create_engine(engine)

    @log
    def execute(self, stmt: str, data=None) -> None:
        with self.engine.connect() as conn:
            conn.execute(text(stmt), data or ())
            conn.commit()
