from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from BackEnd.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True, bind = engine)

Base = declarative_base()