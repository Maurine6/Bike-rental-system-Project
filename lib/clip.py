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

def add_bike(bike_type, availability_status):
    new_bike = Bike(bike_type=bike_type, availability_status=availability_status)
    session.add(new_bike)
    session.commit()
    print(f"Added bike of type {bike_type}")

def update_bike(id, bike_type=None, availability_status=None):
    bike = session.query(Bike).get(id)
    if bike_type:
        bike.bike_type = bike_type
    if availability_status:
        bike.availability_status = availability_status
    session.commit()
    print(f"Updated bike {id}")

def delete_rental_history(customer_id):
    rentals = session.query(Rental).filter(Rental.customer_name == customer_id).all()
    for rental in rentals:
        session.delete(rental)
    session.commit()
    print(f"Deleted rental history for customer {customer_id}")