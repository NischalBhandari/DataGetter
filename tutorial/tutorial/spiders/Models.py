from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey , Float, DateTime
from sqlalchemy import create_engine
import datetime
engine = create_engine('sqlite:///market.db', echo=True)
Base = declarative_base()

class Market(Base):
	__tablename__ = 'market'

	id = Column(Integer, primary_key=True)
	sn = Column(Integer)
	Traded_Companies = Column(String)
	No_Of_Transactions = Column(Integer)
	Max_Price = Column(Float)
	Min_Price = Column(Float)
	Closing_Price = Column(Float)
	Traded_Shares = Column(Integer)
	Amount = Column(Float)
	Previous_Closing = Column(Float)
	Date_Time = Column(DateTime, default=datetime.datetime.now().replace(microsecond=0))

	def __init__(self,sn,Traded_Companies,No_Of_Transactions,Max_Price,Min_Price,Closing_Price,Traded_Shares,Amount,Previous_Closing):
		self.sn = sn
		self.Traded_Companies = Traded_Companies
		self.No_Of_Transactions = No_Of_Transactions
		self.Max_Price = Max_Price
		self.Min_Price = Min_Price
		self.Closing_Price = Closing_Price
		self.Traded_Shares = Traded_Shares
		self.Amount = Amount
		self.Previous_Closing = Previous_Closing
class Testing(Base):
	__tablename__ = 'testing'
	id = Column(Integer, primary_key=True)
	num = Column(Integer)