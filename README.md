VEHICLE SERVICE MANAGEMENT SYSTEM
=================================

1. PROJECT DESCRIPTION
----------------------
This is a basic Python mini-project that helps manage vehicle service
records. It allows the user to add, view, update, and delete service
records using a simple menu-driven program.

The program stores records in a file named services.txt, so saved
records can be loaded again when the program is started.

2. FEATURES
-----------
- Add a new vehicle service record.
- View all saved service records.
- Update the service status.
- Delete a service record.
- Calculate the service cost with 18% GST.
- Save and load records automatically.

3. AVAILABLE SERVICES AND BASE PRICES
-------------------------------------
Oil Change          : Rs. 1,500
Wheel Alignment     : Rs.   800
Full Service        : Rs. 4,500
Brake Repair        : Rs. 2,200

An additional 18% GST is added to the base price.

4. SERVICE STATUSES
-------------------
- Pending
- In Progress
- Completed

5. REQUIREMENTS
---------------
- Python 3
- No external Python libraries are required.
- The program uses Python's built-in json and os modules.

6. HOW TO RUN THE PROJECT
-------------------------
Step 1: Save the Python program as:
        vehicle_service_management.py

Step 2: Open Command Prompt or a terminal in the folder containing
        the Python file.

Step 3: Run this command:

        python vehicle_service_management.py

Step 4: Select an option from the menu by entering a number from 1 to 5.

7. HOW TO USE THE MENU
----------------------
1 - Add Record:
    Enter the vehicle registration number, owner's name, vehicle
    type/model, and service type.

2 - View Records:
    Display all vehicle service records.

3 - Update Status:
    Enter the vehicle registration number and select a valid new status.

4 - Delete Record:
    Enter the vehicle registration number to delete its record.

5 - Exit:
    Close the program. Records are saved automatically after changes.

8. DATA STORAGE
---------------
The program creates and uses a file named services.txt in the same
folder as the Python program. The file stores service records in JSON
format. Do not delete this file if you want to keep your saved records.

9. PROJECT CONCEPTS USED
------------------------
- Python variables and data types
- Input and output
- if-elif-else conditions
- while loop
- Functions and methods
- Classes and objects
- Dictionary data structure
- File handling
- JSON data storage
- Basic input validation

10. IMPORTANT NOTES
-------------------
- Each vehicle registration number must be unique.
- Registration numbers are stored in uppercase.
- Service names are matched without depending on capitalization.
- Only the listed service types and statuses are accepted.
- The displayed service cost includes 18% GST.

11. PROJECT PURPOSE
-------------------
This project is made for learning basic Python programming concepts.
It demonstrates how a simple menu-driven application can manage
records and store data in a file.

=================================
END OF README
============================