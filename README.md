## BIKE RENTAL SYSTEM.
## Description.
The Bike Rental System is a Python application designed to manage a bike rental service. It provides functionalities such as adding and updating customer and bike records, viewing available and rented bikes, managing rentals, and searching for customers by name. This document outlines the setup, usage, and features of the CLI.

## AUTHOR: Omondi Maurine.

## Features
1. Customers
Registration: New customers can register by providing their name and email address.
Rental History: Customers can view their past rentals, including details like rental dates, bike types, and rental durations.
2. Bikes
Inventory Management: Administrators can add new bikes to the inventory, specifying the bike type and availability status.
Bike Types: Differentiates between road, mountain, and electric bikes, allowing for targeted marketing and promotions.
3. Rentals
Booking: Customers can book bikes for rental periods, selecting from daily, or weekly options.
Return Tracking: Rentals include a record of the rental start and end times, facilitating easy tracking of bike usage and returns.
4. Search Functionality: Allows searching for customers by name.

## Modules:
in the file main.py; there are three class modules with tables which has corresponding attributes/instances/columns for data entry.

## Prerequisites
- Python 3.8.13
- SQLAlchemy for ORM
- An active database connection


## Installation
- Ensure Python 3.8.13 is installed on your system.
- Install required packages using pip:

        pip install sqlalchemy 

## Usage
Running the Application
To run the application, execute the following command in your terminal:

        python3 lib/clip.py

This will initialize the database and launch the CLI interface.

## CLI Commands:
Upon running the application, you'll be presented with a menu of options to interact with the bike rental system:

- Add New Customer: Adds a new customer to the database.
- Update Customer Details: Updates existing customer details.
- Add New Bike: Adds a new bike to the inventory.
- Update Bike Details: Updates the details of an existing bike.
- Delete Rental: Deletes a rental record.
- Search Customer by Name: Searches for a customer by name.
- View Available Bikes: Lists all available bikes for rent.
- View All Customers: Displays all registered customers.
- View Rented Bikes: Shows all bikes that are currently rented.
- View Rentals: Lists all rental transactions.
- Rent Bike: Initiates a new bike rental transaction.
- Exit: Exits the CLI.

Each option prompts for necessary inputs to perform the corresponding action. For example, selecting "Add New Customer" will prompt for the customer's name, email, and optional rental history.




TECHNOLOGY USED: PYTHON.

Support and contact details: https://github.com/Maurine6/


LICENCE:

The content of this site is licensed under the MIT license
Copyright (c) 2018.
