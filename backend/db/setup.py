import os
from dotenv import load_dotenv
from sqlalchemy import DateTime, create_engine, Column, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class TableBase(Base):
    """
    Base class for all SQLAlchemy models to include common fields:
    id, created_at, updated_at.
    """

    __abstract__ = True

    id = Column(
        Integer, primary_key=True, autoincrement=True, comment="Unique identifier"
    )
    created_at = Column(
        DateTime, nullable=False, default=func.now(), comment="When record was created"
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        comment="When record was updated",
    )


Session = sessionmaker(bind=engine)
session = Session()
