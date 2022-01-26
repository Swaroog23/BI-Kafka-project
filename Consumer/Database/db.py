from mimetypes import init

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

from Database.tabels import Base, User


def init_database():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Admin123@localhost:5432/",
        echo=True,
        future=True,
    )
    session = sessionmaker(bind=engine)()
    with session.connection() as session_conn:
        session_conn.connection.set_isolation_level(0)
        try:
            session.execute("CREATE DATABASE SBI")
        except exc.ProgrammingError:
            pass
        session_conn.connection.set_isolation_level(1)
        create_tables()
        session.commit()


def create_tables():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Admin123@localhost:5432/sbi",
        echo=True,
        future=True,
    )
    Base.metadata.create_all(engine)

def insert_data(data):
    engine = create_engine(
        "postgresql+psycopg2://postgres:Admin123@localhost:5432/sbi",
        future=True,
    )

    session = sessionmaker(bind=engine)()
    first_name, last_name, age, city = data.values()

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        age=int(age),
        city=city)

    with session as session:
        session.add(new_user)
        session.commit()
