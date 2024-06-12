import argparse
import sys
from main import Base, engine, session
from main import Customer, Bike, Rental

def init_db():
    Base.metadata.create_all(engine)

def add_customer(name, email, rental_history=None):
    new_customer = Customer(name=name, email=email, rental_history=rental_history)
    session.add(new_customer)
    session.commit()
    print(f"Added customer {name}")