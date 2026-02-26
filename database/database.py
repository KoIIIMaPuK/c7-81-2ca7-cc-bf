from sqlalchemy import create_engine, Column, Integer, String, DateTime, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///user_consent_database.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UploadedFile(Base):
    __tablename__ = "user_agree"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False) 
    username = Column(String, nullable=True)
    user_choose = Column(String, nullable=True)

Base.metadata.create_all(engine)