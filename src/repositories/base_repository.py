from src.database.client import Client


class BaseRepository:
    def __init__(self, client: Client):
        self.client = client