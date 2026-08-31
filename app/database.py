
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./data/complaints.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
     autocommit=False, 
     autoflush=False, 
     bind=engine
     )

Base = declarative_base() 

from app import models
Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
     print("Database connection successful!")

