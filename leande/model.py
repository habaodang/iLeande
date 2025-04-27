from leande import db, create_app
from  sqlalchemy import Column,Integer,String,Boolean,Date
from datetime import datetime
from flask_login import UserMixin


class Account(db.Model,UserMixin):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
