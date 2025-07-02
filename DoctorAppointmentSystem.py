
import queue
#this class represents patients
class Patients:
#'Initializing' the attributes of the objects
#"none because no appointments have been set yet"
#'self' as a keyword to access variables, attributes and methods of a defined class which in this case is patient
    def __init__(self, name, age, health_condition, appointment_date = None):
        self.name = name
        self.age = age
        self.health_condition = health_condition
        self.appointment_date = appointment_date

class DoctorAppointmentSystem:
    def __init__(self):
#Using a queue to add appointment requests
#Queue is suitable because appointments will be added at one end and the first one would be removed beccause of the First in, First out principle (FIFO)
        self.waitlist = queue.Queue()
#Using an empty list as a stack for appointment cancellations
#LIFO principle (Last in First out): the last appointment cancelled will be the first one to be considered for rebooking
        self.cancellation_stack = []
#Using an empty list for confirmed appointments
        self.appointment_list = []

#function for requesting appointment
    def request_appointment(self, patient):
#this adds the patient into the waiting list queue
#'put' to insert the patient into the queue
        self.waitlist.put(patient)
#message to show a successful addition to the waiting list
        print(patient.name," has been added to the waiting list for booking.")

#function to reschedule appointment
    def reschedule_appointment(self, name, new_date):

#to track if the name is found by holding it before finding
        found = False
#to go over every single patient in the confirmed appointment list (find the patient)
        for patient in self.appointment_list:
#if the patient name is found, it updates (equates) the appointment date to the new date
            if patient.name == name:
                patient.appointment_date = new_date
#confirmed message of new appointment
                print("Appointment for", name, "has been rescheduled to", new_date)
#marks the patient as found
                found = True
                break
#if the name doesnt exist, a message will be printed
        if not found:
            print("No appointment found for:", name)

#function to confirm appointment
    def confirm_appointment(self):
#if the waitlist is not empty, the user can input their name
        if not self.waitlist.empty():
            confirmed_name = input("Enter your full name: ")
#use this to track if the name is found yet
            found = False
#a temporary queue to hold patients
            temp_queue = queue.Queue()
#a loop that iterates and process through each patient in the waitlist queue
            while not self.waitlist.empty():
#collects the name to use operations on them later
                patient = self.waitlist.get()
#if the name entered matches the patient's name, the boolean variable 'found' would be true
                if patient.name == confirmed_name:
                    found = True
                    if patient not in self.appointment_list:
#confirmation message and a input to confirm the appointment
#ensuring anything inserted is lowercase
                        print("Confirm appointment for", confirmed_name, "? (yes/no): ")
                        confirmation = input().lower()
#if 'yes', the patient is added to the confirmed appointment list and a message is printed
                        if confirmation == "yes":
                            self.appointment_list.append(patient)
                            print(patient.name,"'s appointment has been confirmed.")
#if not, the name will be added back to the waiting list
                        else:
                            print(patient.name,"'s appointment has been added back to the waiting list for booking.")
                            self.waitlist.put(patient)
#this else will move patients to the temporary queue if their appointments have not been processed
                else:
                    temp_queue.put(patient)
#this will move the patients from the temporary queue to the waitlist
            while not temp_queue.empty():
                self.waitlist.put(temp_queue.get())
#if the patient's name does not match, a message will be printed
            if not found:
                print("No appointment found for:", confirmed_name)
        else:
            print("No appointments in the waiting list for booking.")

#function to cancel appointment
    def cancel_appointment(self, cancel_name):
#if the input is empty, this will be printed out
        if not cancel_name:
            print("Error: Cancel name cannot be empty.")
#function will be exited
            return

        found = False
#a new list for patients without cancelled appointments
        uncancelled = []
#to iterate every name in the appointment list
        for patient in self.appointment_list:
#to check if the entered name matches the patient's name
            if patient.name == cancel_name:
                found = True
#this will append the patient to the cancellation stack and print out a message
                self.cancellation_stack.append(patient)
                print("Cancelled appointment for:", cancel_name)
            else:
#if the patient's name doesn't match, it's added to the temporary list
                uncancelled.append(patient)
#update the appointment list with the uncancelled list
        self.appointment_list = uncancelled
#if the appointment is not found, a message is printed
        if not found:
            print("No appointment found for:", cancel_name)

#function to view waiting list
    def print_waiting_list(self):
        print("Waiting List for Booking:")
#if the queue is empty, a message will be printed
        if len(self.waitlist.queue) == 0:
            print("No patients in the waiting list.")
        else:
#if there are patients, their details will be printed
            waiting_list = list(self.waitlist.queue)
#it goes through every patient in the waiting list
            for patient in waiting_list:
                print("Name:", patient.name)
                print("Health Condition:", patient.health_condition)
                print("Appointment Date:", patient.appointment_date)

#function to print confirmed appointment list
    def print_appointment_list(self):
        print("Confirmed Appointment List:")
#if it's empty, a message will be printed out
        if len(self.appointment_list) == 0:
            print("No appointments in the list.")
        else:
#this goes through every patient in the appointment list
            for patient in self.appointment_list:
                print("Name:", patient.name)
                print("Health Condition:", patient.health_condition)
                print("Appointment Date:", patient.appointment_date)

#an instance of the doctor's appointment system from the appointment system where it can be interacted with
appointment_system = DoctorAppointmentSystem()

#a menu to allow the user to choose the function they want to use
while True:
    print()
    print("Welcome to the clinic! Please state your purpose:")
    print("1. Book an appointment.")
    print("2. Confirm an appointment.")
    print("3. View confirmed appointment list.")
    print("4. View waiting list for booking.")
    print("5. Reschedule an appointment.")
    print("6. Cancel an appointment.")
    print("7. Quit the program.")
    print()

#input to choose what function
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Please enter your full name: ")
        age = input("Please enter your age: ")
#this line is the make sure the user is entering a valid age (a positive integer)
#if not a message will be printed
        if not age.isdigit() or int(age) <= 0:
            print("Error: Age must be a positive integer.")
            continue
#details entered by the user
        health_condition = input("Please enter your health condition: ")
        appointment_date = input("Please enter your preferred appointment date (D/M): ")
#another insrance when the details all make up to a new patient profile as the default is "None"
#automatically requests for a new appointment and adds to the waiting list
        appointment_system.request_appointment(Patients(name, int(age), health_condition, appointment_date))

#calls the confirmation appointment system function, book from the waiting list
    elif choice == '2':
        appointment_system.confirm_appointment()

#calls the printing confirmed waiting list function
    elif choice == '3':
        appointment_system.print_appointment_list()

#calls the printing waiting list function
    elif choice == '4':
        appointment_system.print_waiting_list()

#calls the rescheduling appointment function
    elif choice == '5':
        cancel_name = input("Please enter your full name: ")
#ensures the input is not empty
        if not cancel_name:
            print("Error: Cancelled name cannot be empty.")
            continue
#lets the user enter the new preferred date
        new_date = input("Please enter the new appointment date (D/M): ")
        appointment_system.reschedule_appointment(cancel_name, new_date)

#calls the cancelling appointment function
    elif choice == '6':
        cancel_name = input("Please enter your full name: ")
        appointment_system.cancel_appointment(cancel_name)

#exits the program and breaks the loop
    elif choice == '7':
        print("Exiting program.")
        break

#message when something other than the numbers 1-7 is entered
    else:
        print("Invalid choice. Please try again.")