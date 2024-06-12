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

def view_available_bikes():
    available_bikes = session.query(Bike).filter(Bike.availability_status == 'available').all()
    if available_bikes:
        print("Available Bikes:")
        for bike in available_bikes:
            print(f"{bike.id}: {bike.bike_type} - {bike.availability_status}")
    else:
        print("No bikes are available for rent.")

def view_all_customers():
    customers = session.query(Customer).all()
    if customers:
        print("All Customers:")
        for customer in customers:
            print(f"{customer.id}: {customer.name} ({customer.email})")
    else:
        print("No customers found.")

def view_rented_bikes():
    rented_bikes = session.query(Bike).filter(Bike.availability_status!= 'available').all()
    if rented_bikes:
        print("Rented Bikes:")
        for bike in rented_bikes:
            print(f"{bike.id}: {bike.bike_type} - {bike.availability_status}")
    else:
        print("No bikes are currently rented.")

def view_rental_history(customer_email):
    customer = session.query(Customer).filter(Customer.email == customer_email).first()
    if customer:
        rentals = session.query(Rental).filter(Rental.customer_name == customer.name).all()
        if rentals:
            print(f"Rental History for {customer.name} ({customer.email}):")
            for rental in rentals:
                print(f"ID: {rental.id}, Date: {rental.rental_date} - {rental.return_date}, Duration: {rental.rental_duration}")
        else:
            print("No rental history found for this customer.")
    else:
        print("No customer found with the given email.")

def delete_rental_history(customer_id):
    rentals = session.query(Rental).filter(Rental.customer_name == customer_id).all()
    for rental in rentals:
        session.delete(rental)
    session.commit()
    print(f"Deleted rental history for customer {customer_id}")

def search_customer_by_name(name):
    customer = session.query(Customer).filter(Customer.name == name).first()
    if customer:
        print(f"Found customer: {customer.name} ({customer.email})")
        rentals = session.query(Rental).filter(Rental.customer_name == customer.name).all()
        if rentals:
            print("Rentals:")
            for rental in rentals:
                print(f"ID: {rental.id}, Date: {rental.rental_date} - {rental.return_date}, Duration: {rental.rental_duration}")
        else:
            print("No rentals found for this customer.")
    else:
        print("No customer found with the given name.")

def run_cli():
    while True:
        print("\nBike Rental System CLI")
        print("1. Add New Customer")
        print("2. Update Customer Details")
        print("3. Add New Bike")
        print("4. Update Bike Details")
        print("5. Delete Rental History")
        print("6. Search Customer by Name")
        print("7. View Available Bikes")
        print("8. View All Customers")
        print("9. View Rented Bikes")
        print("10. View Rental History")
        print("11. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            rental_history = input("Enter rental history (optional): ")
            add_customer(name, email, rental_history)
        elif choice == '2':
            id = int(input("Enter customer ID: "))
            name = input("Enter new customer name (optional): ")
            email = input("Enter new customer email (optional): ")
            rental_history = input("Enter new rental history (optional): ")
            update_customer(id, name, email, rental_history)
        elif choice == '3':
            bike_type = input("Enter bike type: ")
            availability_status = input("Enter availability status (available/rented): ")
            add_bike(bike_type, availability_status)
        elif choice == '4':
            id = int(input("Enter bike ID: "))
            bike_type = input("Enter new bike type (optional): ")
            availability_status = input("Enter new availability status (optional): ")
            update_bike(id, bike_type, availability_status)
        elif choice == '5':
            customer_id = input("Enter customer ID: ")
            delete_rental_history(customer_id)
        elif choice == '6':
            name = input("Enter customer name to search: ")
            search_customer_by_name(name)
        elif choice == '7':
            view_available_bikes()
        elif choice == '8':
            view_all_customers()
        elif choice == '9':
            view_rented_bikes()
        elif choice == '10':
            customer_email = input("Enter customer email: ")
            view_rental_history(customer_email)
        elif choice == '11':
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    init_db()
    run_cli()