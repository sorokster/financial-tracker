from database import init_db, db_session


class BaseRepository:
    def __init__(self):
        self.db = init_db()
        self.session = db_session()