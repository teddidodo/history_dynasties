from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://Thanh_Do:v2_3wCf7_nJDkz8wzQ6tAaenvA4mpsY4@db.bit.io/Thanh_Do/history_timeline"
engine = create_engine(SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT", pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base = declarative_base()