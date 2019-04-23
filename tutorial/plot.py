import sqlite3
from tutorial.spiders.Models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt 
engine = create_engine('sqlite:///market.db', echo=True)
session = sessionmaker(bind=engine)
session = session()
x = session.query(Market).filter_by(Traded_Companies="Agriculture Development Bank Limited").all()
dates = []
closing = []
for i in x:
	dates.append(i.Date_Time)
	closing.append(i.Closing_Price)

plt.plot(dates,closing)
plt.show()