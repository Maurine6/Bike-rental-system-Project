# import necessary modules
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.sqlite import INTEGER, TEXT

# declare Base
Base = declarative_base()

# create a class Rental
class Rental(Base):
    # create table rentals
    __tablename__ = 'rentals'
    
    #declare table contents
    id = Column(INTEGER, primary_key=True)
    rental_date = Column(Date)
    return_date = Column(Date)
    rental_duration = Column(INTEGER)
    customer_name = Column(String, ForeignKey('customers.name'))
    bike_id = Column(INTEGER, ForeignKey('bikes.id'))

    # define table relationships
    customer = relationship("Customer", back_populates="rentals")
    bike = relationship("Bike", back_populates="rentals")

# create class Customer
class Customer(Base):
    # create table customers and declare customer table contents
    __tablename__ = 'customers'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    rental_history = Column(TEXT)

    # define customer- rental relationship
    rentals = relationship("Rental", order_by=Rental.id, back_populates="customer")

# create class Bike
class Bike(Base):
    # create bikes table and declare bikes table contents.
    __tablename__ = 'bikes'
    
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    bike_type = Column(String)
    availability_status = Column(String)

    # define bikes-rental relationship
    rentals = relationship("Rental", order_by=Rental.id, back_populates="bike")

# create a database using inbuilt create engine function
engine = create_engine("sqlite:///mydb.db", echo=True)
#store all data in the engine
Base.metadata.create_all(engine)

#bind all data to the engine(database) by initializing seesion
Session = sessionmaker(bind=engine)
session = Session()
