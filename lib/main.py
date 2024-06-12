from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.sqlite import INTEGER, TEXT

Base = declarative_base()

class Rental(Base):
    __tablename__ = 'rentals'
    
    id = Column(INTEGER, primary_key=True)
    rental_date = Column(Date)
    return_date = Column(Date)
    rental_duration = Column(INTEGER)
    customer_name = Column(String, ForeignKey('customers.name'))
    bike_id = Column(INTEGER, ForeignKey('bikes.id'))

    customer = relationship("Customer", back_populates="rentals")
    bike = relationship("Bike", back_populates="rentals")

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    rental_history = Column(TEXT)

    rentals = relationship("Rental", order_by=Rental.id, back_populates="customer")

class Bike(Base):
    __tablename__ = 'bikes'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    bike_type = Column(String)
    availability_status = Column(String)

    rentals = relationship("Rental", order_by=Rental.id, back_populates="bike")


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
