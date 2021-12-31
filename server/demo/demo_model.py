# imports
from sqlalchemy import Integer, Column, String
from server import db
from .demo_interface import DemoInterface


#  demo model for SQLAlchemy
class Demo(db.Model):
    __tablename__ = "demos"

    id = Column(Integer, primary_key=True)
    value = Column(String(50))

    # update function
    def update(self, changes: DemoInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

