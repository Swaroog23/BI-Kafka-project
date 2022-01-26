from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    city = Column(String(100))

    def __repr__(self) -> str:
        return f"""User(
            id={self.id!r}, 
            first_name={self.first_name!r},
            last_name={self.last_name!r},
            age={self.age!r},
            city={self.city!r})
            """
