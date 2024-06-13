# bike rental system cli
# import all the necessary modules
import argparse
import sys
import datetime
from main import Base, engine, session
from main import Customer, Bike, Rental

#initialize database
def init_db():
    # call the parent class Base to store our data
    Base.metadata.create_all(engine)

# start defining needed functions to run our cli
# define add-customer function
def add_customer(name, email, rental_history=None):
    # create a new customer
    new_customer = Customer(name=name, email=email, rental_history=rental_history)
    # add new customer to the database
    session.add(new_customer)
    # commit the created customer
    session.commit()
    # print customer details when the function is called
    print(f"Added customer {name}")

# define update customer function
def update_customer(id, name=None, email=None, rental_history=None):
    # query the customer id.
    customer = session.query(Customer).get(id)
    if name:
        customer.name = name
    if email:
        customer.email = email
    if rental_history:
        customer.rental_history = rental_history
    # commit the update    
    session.commit()
    # print the update when requested
    print(f"Updated customer {id}")

# define add bike function
def add_bike(bike_type, availability_status):
    # create a new bike
    new_bike = Bike(bike_type=bike_type, availability_status=availability_status)
    # add the new bike to the database
    session.add(new_bike)
    #commit the new bike and print new bike when requested
    session.commit()
    print(f"Added bike of type {bike_type}")

# define update bike function
def update_bike(id, bike_type=None, availability_status=None):
    # update bike details
    bike = session.query(Bike).get(id)
    if bike_type:
        bike.bike_type = bike_type
    if availability_status:
        bike.availability_status = availability_status
        # commit the updates. print when requested
    session.commit()
    print(f"Updated bike {id}")

# define view available function
def view_available_bikes():
    # create a query to view available bikes
    available_bikes = session.query(Bike).filter(Bike.availability_status == 'available').all()
    # check if the bikes are availble
    if available_bikes:
        print("Available Bikes:")
        for bike in available_bikes:
            print(f"{bike.id}: {bike.bike_type} - {bike.availability_status}")
    else:
        print("No bikes are available for rent.")

# define view customer functon
def view_all_customers():
    # create a query to view customers
    customers = session.query(Customer).all()
    # check if the customers are available
    if customers:
        print("All Customers:")
        for customer in customers:
            print(f"{customer.id}: {customer.name} ({customer.email})")
    else:
        print("No customers found.")

# define a view rented function
def view_rented_bikes():
    # create a query to view all rented bikes
    rented_bikes = session.query(Bike).filter(Bike.availability_status!= 'available').all()
    # check if theres any rented bikes
    if rented_bikes:
        print("Rented Bikes:")
        for bike in rented_bikes:
            print(f"{bike.id}: {bike.bike_type} - {bike.availability_status}")
    else:
        print("No bikes are currently rented.")

# define a view rentals function
def view_rentals():
    # create a query to view rentals
    rentals = session.query(Rental).all()
    # check if there's rentals
    if rentals:
        print("All Rentals:")
        for rental in rentals:
            print(f"ID: {rental.id}, Customer: {rental.customer_name}, Bike: {rental.bike_id}, "
                  f"Date: {rental.rental_date}, Return Date: {rental.return_date}, Duration: {rental.rental_duration}")
    else:
        print("No rentals found.")        

# define function to delete rental
def delete_rental(rental_id):
    # create a query to delete the selected rental
    rental = session.query(Rental).get(rental_id)
    # check if the sected rental is available
    if rental:
        session.delete(rental)
        session.commit()
        print(f"Deleted rental with ID {rental_id}")
    else:
        print(f"No rental found with ID {rental_id}")

#define a search customer 
def search_customer_by_name(name):
    # create a query to search customer by name
    customer = session.query(Customer).filter(Customer.name == name).first()
    # check if the customer is available
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

# create and define a funtion to enable renting a bike
def rent_bike():
    try:
        # Get the list of customers and bikes from the database
        customers = session.query(Customer).order_by(Customer.id).all()
        bikes = session.query(Bike).order_by(Bike.id).all()

        # Display customers and ask for selection
        print("Available Customers:")
        for idx, customer in enumerate(customers, start=1):
            print(f"{idx}. {customer.name} ({customer.email})")
        
        customer_choice = int(input("Select a customer by number: ")) - 1
        if 0 <= customer_choice < len(customers):
            selected_customer = customers[customer_choice]
            print(f"You selected {selected_customer.name} ({selected_customer.email}).\n")
        else:
            print("Invalid selection. Please try again.\n")
            return

        # Display bikes and ask for selection
        print("Available Bikes:")
        for idx, bike in enumerate(bikes, start=1):
            print(f"{idx}. {bike.bike_type} ({bike.availability_status})")
        
        bike_choice = int(input("Select a bike by number: ")) - 1
        if 0 <= bike_choice < len(bikes):
            selected_bike = bikes[bike_choice]
            print(f"You selected {selected_bike.bike_type} ({selected_bike.availability_status}).\n")
        else:
            print("Invalid selection. Please try again.\n")
            return

        # Create a new rental record
        new_rental = Rental(
            rental_date= datetime.date.today(),
            return_date= datetime.date.today() + datetime.timedelta(days=1),  # Example rental period
            rental_duration=1,  # Example rental duration in days
            customer_name=selected_customer.name,
            bike_id=selected_bike.id
        )

        # Add the new rental to the session and commit
        session.add(new_rental)
        session.commit()

        print(f"Rental added successfully for {selected_customer.name} with bike {selected_bike.bike_type}.\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# run cli
def run_cli():
    while True:
        print("\nBike Rental System CLI")
        print("1. Add New Customer")
        print("2. Update Customer Details")
        print("3. Add New Bike")
        print("4. Update Bike Details")
        print("5. Delete Rental")
        print("6. Search Customer by Name")
        print("7. View Available Bikes")
        print("8. View All Customers")
        print("9. View Rented Bikes")
        print("10. View Rentals")
        print("11. Rent bike")
        print("12. Exit")
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
            delete_rental(customer_id)
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
            view_rentals()
        elif choice == '11':
            rent_bike()    
        elif choice == '12':
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    init_db()
    run_cli()