from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, REAL
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    def __repr__(self):
        return '<Category %r>' % self.name

class Transaction(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    amount = Column(REAL, nullable=False)
    category = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))
    owner = Column(ForeignKey('users.id', ondelete='CASCADE'))
    description = Column(String(100), nullable=True)
    type = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Transaction %r>' % self.id
