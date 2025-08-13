class User:
    def __init__(self, user_id: int, email: str, name: str, surname: str, password: str):
        self.id = user_id
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password

    @classmethod
    def from_row(cls, row: dict):
        return cls(
            user_id=row['id'],
            email=row['email'],
            name=row['name'],
            surname=row['surname'],
            password=row['password'],
        )

    def to_dict(self, include_sensitive=False):
        data = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'surname': self.surname,
        }
        if include_sensitive:
            data['password'] = self.password
        return data

    def __repr__(self):
        return f"<User {self.id} {self.email}>"