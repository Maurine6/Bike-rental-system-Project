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

def update_customer(id, name=None, email=None, rental_history=None):
    customer = session.query(Customer).get(id)
    if name:
        customer.name = name
    if email:
        customer.email = email
    if rental_history:
        customer.rental_history = rental_history
    session.commit()
    print(f"Updated customer {id}")