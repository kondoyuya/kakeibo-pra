from sqlalchemy import Column, Integer, String, Text, Date
from application.models.database import Base
import datetime


class UsageHistory(Base):
    __tablename__ = 'usagehistory'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    value = Column(Integer)
    date = Column(Date,default = datetime.date.today())

    def __init__(self, title=None, value=None, date=None):
        self.title = title
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)