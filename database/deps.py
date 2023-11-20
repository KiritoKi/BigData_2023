from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.session import SessionLocal


def get_db() -> Session:
    try:
        db = SessionLocal()
        db.execute(text("SET search_path TO public"))
        return db
    finally:
        db.close()