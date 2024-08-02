from sqlmodel import create_engine, SQLModel, Session
from quiz_backend.settings import db_url, test_db_url
connection_string = str(db_url).replace("postgresql", "postgresql+psycopg2")

engine = create_engine(connection_string, echo=True)

def createTable():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
        
        