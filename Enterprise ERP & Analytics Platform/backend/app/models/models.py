
# Example DB models (SQLAlchemy)
from sqlalchemy import Column, Integer, String

class Employee:
    id = Column(Integer, primary_key=True)
    name = Column(String)
