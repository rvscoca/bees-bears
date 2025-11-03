from app.database.database import get_session


class BaseRepository:
    def __init__(self):
        self.session = get_session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()
